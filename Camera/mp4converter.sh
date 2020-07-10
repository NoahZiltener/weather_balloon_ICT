mkdir out
for n in *.h264
do
	MP4Box -add $n out/$n.mp4
done
