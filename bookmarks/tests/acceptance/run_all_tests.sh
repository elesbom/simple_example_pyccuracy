#!/bin/bash
for i in $( ls | grep --regex="test_.*\.acc$" ); do
echo =================================================
    echo Running $i
    echo =================================================
    pyccuracy_console -p $i --language=pt-br
    echo Done...
done
