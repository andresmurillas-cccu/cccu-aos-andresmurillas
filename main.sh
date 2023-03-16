#!/bin/bash
FSWEB=$(dpkg -l | grep fswebcam)
if [ -z '$FSWEB' ]; then
    sudo apt-get install fswebcam
fi
SIZES=('640x1480' '1024x768' '1920x1040' '2920x1040')
echo -n 'Enter the number of photos: '; read -n 1 FRAMES
echo ""
echo "1. ${SIZES[0]}"
echo "2. ${SIZES[1]}"
echo "3. ${SIZES[2]}"
echo "3. ${SIZES[3]}"
echo -n "Select the resolution: "; read -n 1 SELECT
echo ""
echo -n "Enter the delay between all photos (s): "; read -n 1 DELAY
echo ""
F=0
INDEX=$(($SELECT - 1))
RES=$(echo ${SIZES[$INDEXES]})
echo FRAMES
while [[ $F < $FRAMES ]]; do
    F=$(($F + 1))
    IMAGE="Manu-$(date +'%Y-%m-%d_%H:%M:%S').jpg"
    fswebcam -r $RES $IMAGE
    if [[ $DELAY > 0 ]]; then
        sleep $DELAY
    fi
done