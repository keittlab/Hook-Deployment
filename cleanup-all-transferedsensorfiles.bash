#!/bin/bash
SENSORFILES_DIR="/DATA/environmental"
SOUNDFILES_DIR="/home/pi/upstream/sound"
TIMESTAMP=`(date +%Y%m%d)`
echo "Getting the most recent sensorfiles from $SENSORFILES_DIR"
ls -Art $SENSORFILES_DIR|grep csv > $SENSORFILES_DIR/../logs/environmental-xfer-temp.log-$TIMESTAMP

if [[ $(cat $SENSORFILES_DIR/../logs/environmental-xfer-temp.log-$TIMESTAMP| wc -l) -eq 0 ]]; then
        echo " "
        echo "NOTE: There are no wav sound files to clean up in $SENSORFILES_DIR"
        echo " "
        exit 0
fi

echo "Sending files."

#cat $SOUNDFILES_DIR/../data/sound-xfer-temp.log-$TIMESTAMP | while read line;do /usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/sendtocorral-minio.py $SOUNDFILES_DIR/$line; done
cat $SENSORFILES_DIR/../logs/environmental-xfer-temp.log-$TIMESTAMP | while read line; do
	if [[ `(/usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/stengl-minio-md5check-cleanoutput.py $SENSORFILES_DIR/$line)` == true ]]; then
	      echo "File $SENSORFILES_DIR/$line already sync'd"
        else 
               /usr/bin/python3 $SOUNDFILES_DIR/../stengl-minio-tests/sendtocorral-minio.py $SENSORFILES_DIR/$line
	fi;
done
