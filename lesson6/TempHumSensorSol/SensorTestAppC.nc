#include "SensorTest.h"

configuration SensorTestAppC {}

implementation {

  components MainC, SensorTestC as App;
  components new TimerMilliC() as temp_t;
  components new TimerMilliC() as hum_t;
  components new TempHumSensorC();
  components ActiveMessageC;
  components new AMSenderC(AM_SEND_MSG);
  components new AMReceiverC(AM_SEND_MSG);

  //Boot interface
  App.Boot -> MainC.Boot;

  //Timer interface
  App.TempTimer -> temp_t;
  App.HumTimer -> hum_t;
	
  //Sensor read
  App.TempRead -> TempHumSensorC.TempRead;
  App.HumRead -> TempHumSensorC.HumRead;

  //Radio Control
  App.SplitControl -> ActiveMessageC;
  App.AMSend -> AMSenderC;
  App.Packet -> AMSenderC;
  App.Receive -> AMReceiverC;
}

