
generic configuration TempHumSensorC() {

	provides interface Read<uint16_t> as TempRead;
	provides interface Read<uint16_t> as HumRead;

} implementation {

	components MainC;
	components new TempHumSensorP();
	components new TimerMilliC() as ReadTempTimer;
	components new TimerMilliC() as ReadHumTimer;
	
	//Connects the provided interface
	TempRead = TempHumSensorP.TempRead;
	HumRead = TempHumSensorP.HumRead;

	//Timer interface	
	TempHumSensorP.TimerReadTemp -> ReadTempTimer;
	TempHumSensorP.TimerReadHum -> ReadHumTimer;


}
