#!/bin/bash
echo "Отчет сохранен в файл report.txt"
touch report.txt
echo "Отчет о логе веб-сервера" > report.txt
echo "========================" >> report.txt
requests=$(wc -l < access.log)
echo "Общее количество запросов: $requests" >> report.txt
awk '
{
    if (!seen[$1]++) {
        uniqueCount++
    }
}
END {
    print "Количество уникальных IP-адресов: " uniqueCount
}' access.log >> report.txt

awk '{
    method = $6
    methods[method]++
}
END {
    print "Количество запросов по методам:"
    for (m in methods) {
        print substr(m, 2) ": " methods[m]
    }
}' access.log >> report.txt

echo "Самый популярный URL:" $(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 1) >> report.txt
