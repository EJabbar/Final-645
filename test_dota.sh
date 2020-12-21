test_images=`ls ./examplesplit/tests/*.png`
for image in $test_images
do
    ../darknet/darknet detector test cfg/dota.data cfg/yolo-dota.cfg backup/yolo-dota.cfg_450000.weights $image -thresh 0.1
    image_name=`basename $image`
    mv_path="./examplesplit/results/result_$image_name"
    mv ./predictions.jpg $mv_path
done
