#!/bin/bash

while [ -n "$1" ]
do
case "$1" in
    --input_folder) inpf=$2 ;;          #абсолютный путь к директории 
    --extension) ext=$2 ;;              #расширение
    --backup_folder) bckf=$2 ;;         #название папки для бэкапа
    --backup_archive_name) bckar=$2 ;;  #имя архива с бэкапом
esac
shift 2
done
mkdir -p "$bckf"
for filename in `find $inpf -name "*.$ext" -print`
do
     newFileName=${filename//"/"/-}
     cp $filename $bckf/$newFileName
done

tar -zcf $bckar $bckf

echo done