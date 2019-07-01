cd "$(dirname "$0")"

for filename in used/*
do
    ./$filename/create.sh
    ./$filename/service.sh
done
