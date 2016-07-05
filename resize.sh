directory="output"
files=$(find $directory | grep svg | grep -v thumb)
for file in $files; do 
  filename=$(basename $file)
  extension="${filename##*.}"
  filename="${filename%.*}"
  thumbname=$filename"-thumb".$extension
  #echo $filename $extension $thumbname
  svg-resize.py --width=30 --height=30 $file $directory/$thumbname
done
