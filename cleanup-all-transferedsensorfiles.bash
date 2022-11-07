#!/bin/bash
SENSORFILES_DIR="/DATA/environmental"
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

#cat $SENSORFILES_DIR/../logs/environmental-xfer-temp.log-$TIMESTAMP | while read line;do /usr/bin/pyth>cat $SENSORFILES_DIR/../logs/environmental-xfer-temp.log-$TIMESTAMP | while read line; do
        if [[ `(/usr/bin/python3 /home/pi/upstream/stengl-minio-tests/stengl-minio-sizeonly-check-clean>              echo "File $SENSORFILES_DIR/$line already sync'd"
        else
               /usr/bin/python3 /home/pi/upstream/stengl-minio-tests/sendtocorral-minio.py $SENSORFILES>        fi;
done