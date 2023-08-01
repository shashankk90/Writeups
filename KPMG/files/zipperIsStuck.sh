#! /bin/bash
# zipperIsStuck.sh
for password in {100..999}; do
  unzip -P "$password" -d "dir$password" "Zipper Is Stuck.zip" > /dev/null 2>&1
  if [ -z "$(ls dir$password)" ]; then
    rmdir "dir$password"
  fi
done

cat dir*/*
rm -rd dir*
