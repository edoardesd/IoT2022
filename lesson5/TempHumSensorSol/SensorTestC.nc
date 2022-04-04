#include "Timer.h"
#include "SensorTest.h"

module SensorTestC {

  uses {
	interface Boot;

	interface SplitControl;
	interface Packet;
    interface AMSend;
    interface Receive;
    	
    interface Timer<TMilli> as TempTimer;
	interface Timer<TMilli> as HumTimer;
	
	interface Read<uint16_t> as TempRead;
	interface Read<uint16_t> as HumRead;
	
  }

} implementation {
  
  message_t packet;  

  void sendData(uint16_t data, uint8_t type){
	  sensor_msg_t* mess = (sensor_msg_t*)(call Packet.getPayload(&packet, sizeof(sensor_msg_t)));
	  if (mess == NULL) {
		return;
	  }
	  mess->type = type;
	  mess->data = data;
	  
	  dbg("radio_pack","Preparing the message... \n");
	  
	  if(call AMSend.send(0, &packet,sizeof(sensor_msg_t)) == SUCCESS){
	     dbg("radio_send", "Packet passed to lower layer successfully!\n");
	     dbg("radio_pack",">>>Pack\n \t Payload length %hhu \n", call Packet.payloadLength( &packet ) );
	     dbg_clear("radio_pack","\t Payload Sent\n" );
		 dbg_clear("radio_pack", "\t\t type: %hhu \n ", mess->type);
		 dbg_clear("radio_pack", "\t\t data: %hhu \n", mess->data);
		 
  	}
  }

  //***************** Boot interface ********************//
  event void Boot.booted() {
      dbg("boot","Application booted on node %u.\n", TOS_NODE_ID);
      call SplitControl.start();
  	
  }

  //***************** SplitControl interface ********************//
  event void SplitControl.startDone(error_t err){
      
    if(err == SUCCESS) {
    	dbg("radio", "Radio on!\n");
	if (TOS_NODE_ID > 0){
           call TempTimer.startPeriodic( 1000 );
           call HumTimer.startPeriodic( 2000 );
  	}
    }
    else{
	//dbg for error
	call SplitControl.start();
    }

  }
  
  event void SplitControl.stopDone(error_t err){}

  //***************** MilliTimer interface ********************//
  event void TempTimer.fired() {
  	dbg("timer","Temperature timer fired at %s.\n", sim_time_string());
	call TempRead.read();

  }
  event void HumTimer.fired() {
  	dbg("timer","Humidity timer fired at %s.\n", sim_time_string());
	call HumRead.read();
  }
  
  //************************* Read interface **********************//
  event void TempRead.readDone(error_t result, uint16_t data) {
	double temp = ((double)data/65535)*100;
	dbg("temp","temp read done %f\n",temp);
	
	sendData((uint16_t) temp, 0);
  }

  event void HumRead.readDone(error_t result, uint16_t data) {
	double hum = ((double)data/65535)*100;
	dbg("hum","hum read done %f\n",hum);
	
	sendData((uint16_t) hum, 1);
  }

  event void AMSend.sendDone(message_t* buf, error_t error) {
    if (&packet == buf && error == SUCCESS) {
      dbg("radio_send", "Packet sent...");
      dbg_clear("radio_send", " at time %s \n", sim_time_string());
    }
    else{
      dbgerror("radio_send", "Send done error!");
    }
  }

event message_t* Receive.receive(message_t* bufPtr, void* payload, uint8_t len) {
	
    if (len != sizeof(sensor_msg_t)) {return bufPtr;}
    else {
      sensor_msg_t* mess = (sensor_msg_t*)payload;
      
      dbg("radio_rec", "Received packet at time %s\n", sim_time_string());
      dbg("radio_pack"," Payload length %hhu \n", call Packet.payloadLength( bufPtr ));
      dbg("radio_pack", ">>>Pack \n");
      dbg_clear("radio_pack","\t\t Payload Received\n" );
      dbg_clear("radio_pack", "\t\t type: %hhu \n ", mess->type);
	  dbg_clear("radio_pack", "\t\t data: %hhu \n", mess->data);
     
      return bufPtr;
    }
    {
      dbgerror("radio_rec", "Receiving error \n");
    }
  }

}

