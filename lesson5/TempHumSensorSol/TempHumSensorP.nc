#include "DATA/TEMP_DATA.h"
#include "DATA/HUM_DATA.h"
 
generic module TempHumSensorP() {

	provides interface Read<uint16_t> as TempRead;
	provides interface Read<uint16_t> as HumRead;
	
	uses interface Timer<TMilli> as TimerReadTemp;
	uses interface Timer<TMilli> as TimerReadHum;


} implementation {

	uint16_t temp_index = 0;
	uint16_t hum_index = 0;
	uint16_t temp_read_value = 0;
	uint16_t hum_read_value = 0;


	//***************** Read interface ********************//
	command error_t TempRead.read(){

		temp_read_value = TEMP_DATA[temp_index];
		temp_index++;
		if(temp_index==TEMP_DATA_SIZE)
			temp_index = 0;

		call TimerReadTemp.startOneShot( 2 );
		return SUCCESS;
	}

	command error_t HumRead.read(){
		hum_read_value = HUM_DATA[hum_index];
		hum_index++;
		if(hum_index==HUM_DATA_SIZE)
			hum_index = 0;

		call TimerReadHum.startOneShot( 2 );
		return SUCCESS;
	}

	//***************** Timer interfaces ********************//
	event void TimerReadTemp.fired() {
		signal TempRead.readDone( SUCCESS, temp_read_value );
	}

	event void TimerReadHum.fired() {
		signal HumRead.readDone( SUCCESS, hum_read_value );
	}
}
