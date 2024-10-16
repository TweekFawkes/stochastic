#!/bin/bash

# Generate timestamp
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

# Function to run zmap with dynamic timestamp
run_zmap() {
    local ports=$1
    zmap -B 10M --target-ports=$ports --list-of-ips-file=input_ips.txt \
    --output-file=${TIMESTAMP}___${ports//,/_} \
    --log-directory=/ops/zmap/logs/ \
    --status-updates-file=/ops/zmap/logs/status.txt \
    --blocklist-file=/ops/zmap/blocklist.conf
}

# Run zmap for different port sets
run_zmap "80,443,21"
sleep 21m

run_zmap "23,8080,53"
sleep 21m

run_zmap "4567,143,22"
sleep 21m

run_zmap "110,5060,993"
sleep 21m

run_zmap "587,8081,8085"
sleep 21m

run_zmap "3389,5357,135"
sleep 21m

run_zmap "8000,199,81"
sleep 21m

run_zmap "465,111,49152"
sleep 21m

run_zmap "2000,3306,10000"
sleep 21m

run_zmap "8008,554,5000"
sleep 21m

run_zmap "5900,8888,8443"
sleep 21m

run_zmap "9999,8088,88"
sleep 21m

run_zmap "515,9001,444"
sleep 21m

run_zmap "139,26,9000"
sleep 21m

run_zmap "3128,6969,8880"
sleep 21m

run_zmap "631,2001,1025"
sleep 21m

run_zmap "8082,82,5800"
sleep 21m

run_zmap "2601,2002,106"
sleep 21m

run_zmap "9090,548,8009"
sleep 21m

run_zmap "1026,1311,2121"
sleep 21m

run_zmap "5190,3000,1433"
sleep 21m

run_zmap "5432,1050,18182"
sleep 21m

run_zmap "8001,4001,79"
sleep 21m

run_zmap "50000,1027,113"
sleep 21m

run_zmap "8083,5555,85"
sleep 21m

run_zmap "6001,445,9100"
sleep 21m

run_zmap "389,5009,990"
sleep 21m

run_zmap "5001,4000,6004"
sleep 21m

run_zmap "1024,2049,8010"
sleep 21m

run_zmap "1723,2525,8181"
sleep 21m

run_zmap "1080,83,12345"
sleep 21m

run_zmap "8005,8002,1022"
sleep 21m

run_zmap "5901,6667,6666"
sleep 21m

run_zmap "513,8007,7070"
sleep 21m

run_zmap "7777,902,10001"
sleep 21m

run_zmap "873,19,3690"
sleep 21m

run_zmap "9080,7000,2869"
sleep 21m

run_zmap "666,8194,11211"
sleep 21m

run_zmap "6668,593,1900"
sleep 21m

run_zmap "84,4444,636"
sleep 21m

run_zmap "2030,2100,7"
sleep 21m

run_zmap "6002,6000,1031"
sleep 21m

run_zmap "49157,18264,8084"
sleep 21m

run_zmap "514,3050,1494"
sleep 21m

run_zmap "9091,5222,264"
sleep 21m

run_zmap "2103,5269,119"
sleep 21m

run_zmap "1099,9102,9002"
sleep 21m

run_zmap "280,100,6543"
sleep 21m

run_zmap "6669,3333,3689"
sleep 21m

run_zmap "50003,8003,2005"
sleep 21m

run_zmap "5050,2107,9092"
sleep 21m

run_zmap "9097,5003,3268"
sleep 21m

run_zmap "9093,995,8004"
sleep 21m

run_zmap "31337,1110,8006"
sleep 21m

run_zmap "32768,10010,2301"
sleep 21m

run_zmap "1000,2003,1521"
sleep 21m

run_zmap "787,2161,179"
sleep 21m

run_zmap "523,1029,808"
sleep 21m

run_zmap "3372,20000,7002"
sleep 21m

run_zmap "6664,8883,8031"
sleep 21m

run_zmap "55555,1352,1028"
sleep 21m

run_zmap "254,311,5550"
sleep 21m

run_zmap "5120,1234,5666"
sleep 21m

run_zmap "1111,5801,60023"
sleep 21m

run_zmap "42,1030,8887"
sleep 21m

run_zmap "9096,888,9003"
sleep 21m

run_zmap "6660,1935,1035"
sleep 21m

run_zmap "3002,7100,4045"
sleep 21m

run_zmap "3351,60000,60021"
sleep 21m

run_zmap "15000,32771,8881"
sleep 21m

run_zmap "1040,6050,6662"
sleep 21m

run_zmap "8886,5061,9099"
sleep 21m

run_zmap "2383,3052,8884"
sleep 21m

run_zmap "544,8885,9103"
sleep 21m

run_zmap "9101,8882,646"
sleep 21m

run_zmap "5631,6005,4443"
sleep 21m

run_zmap "1056,6663,6112"
sleep 21m

run_zmap "5101,2717,3001"
sleep 21m

run_zmap "1033,1100,17988"
sleep 21m

run_zmap "2105,900,3703"
sleep 21m

run_zmap "1054,1583,1066"
sleep 21m

run_zmap "1037,6014,9095"
sleep 21m

run_zmap "1064,1048,1526"
sleep 21m

run_zmap "1074,1036,1065"
sleep 21m

run_zmap "9050,1071,1044"
sleep 21m

run_zmap "1095,5051,4711"
sleep 21m

run_zmap "1049,1058,1059"
sleep 21m

run_zmap "1801,1069,497"
sleep 21m

run_zmap "1,3986,6588"
sleep 21m

run_zmap "6346,1998,27001"
sleep 21m

run_zmap "9089,27000,1039"
sleep 21m

run_zmap "144,1220,2160"
sleep 21m

run_zmap "1042,13722,6661"
sleep 21m

run_zmap "9094,6379,1053"
sleep 21m

run_zmap "9088,1214,9098"
sleep 21m

run_zmap "9801,6665,5802"
sleep 21m

run_zmap "9030,32770,27017"
sleep 21m

run_zmap "540,1038,6699"
sleep 21m

run_zmap "5280,2701,1344"
sleep 21m

run_zmap "11371,1503,2396"
sleep 21m

run_zmap "2010,9,8118"
sleep 21m

run_zmap "1981,901,2401"
sleep 21m

run_zmap "10005,1720,6646"
sleep 21m

run_zmap "2064,10031,7402"
sleep 21m

run_zmap "3006,6600,3"
sleep 21m

run_zmap "1090,60009,32777"
sleep 21m

run_zmap "14534,32772,6670"
sleep 21m

run_zmap "7937,1501,6003"
sleep 21m

run_zmap "6103,625,7938"
sleep 21m

run_zmap "2306,70,3031"
sleep 21m

run_zmap "3005,6011,1241"
sleep 21m

run_zmap "2040,7210,32764"
sleep 21m

run_zmap "6010,50030,1109"
sleep 21m

run_zmap "1754,7144,32769"
sleep 21m

run_zmap "5803,6006,5232"
sleep 21m

run_zmap "2715,6017,13666"
sleep 21m

run_zmap "2967,50025,15002"
sleep 21m

run_zmap "898,6544,1098"
sleep 21m

run_zmap "7007,4660,6007"
sleep 21m

run_zmap "641,9107,6015"
sleep 21m

run_zmap "6009,50001,7272"
sleep 21m

run_zmap "1248,1314,13013"
sleep 21m

run_zmap "6016,32767,6802"
sleep 21m

run_zmap "6012,1610,3872"
sleep 21m

run_zmap "1830,1755,5427"
sleep 21m

run_zmap "3280,1611,1105"
sleep 21m

run_zmap "505,32775,3531"
sleep 21m

run_zmap "8770,1217,6008"
sleep 21m

run_zmap "7776,1500,3310"
sleep 21m

run_zmap "5530,40193,7180"
sleep 21m

run_zmap "50022,60001,2024"
sleep 21m

run_zmap "32774,5520,9105"
sleep 21m

run_zmap "2068,32773,1200"
sleep 21m

run_zmap "8307,9106,6018"
sleep 21m

run_zmap "50005,1761,6020"
sleep 21m

run_zmap "6013,255,5556"
sleep 21m

run_zmap "9104,591,32757"
sleep 21m

run_zmap "60022,543,22001"
sleep 21m

run_zmap "783,3004,5570"
sleep 21m

run_zmap "32776,771,6163"
sleep 21m

run_zmap "6019,18086,60002"
sleep 21m

run_zmap "1112,50002,620"
sleep 21m

run_zmap "1032,8087,1414"
sleep 21m

run_zmap "406,1417,15001"
sleep 21m

run_zmap "449,256,2627"
sleep 21m

run_zmap "512,7008,1748"
sleep 21m

run_zmap "7145,49400,464"
sleep 21m

run_zmap "7780,6560,4155"
sleep 21m

run_zmap "4999,2600,1418"
sleep 21m

run_zmap "1522,3003,1972"
sleep 21m

run_zmap "32787,11965,1212"
sleep 21m

run_zmap "1415,3025,32779"
sleep 21m

run_zmap "60019,1419,1416"
sleep 21m

run_zmap "161,7200,32765"
sleep 21m

run_zmap "1527,98,32778"
sleep 21m

run_zmap "19350,1505,1420"
sleep 21m

run_zmap "5400,5600,2427"
sleep 21m

run_zmap "1010,3940,7171"
sleep 21m

run_zmap "3900,50015,1400"
sleep 21m

run_zmap "27004,43,1302"
sleep 21m

run_zmap "32752,1043,1041"
sleep 21m

run_zmap "32797,2947,7101"
sleep 21m

run_zmap "8138,27008,1702"
sleep 21m

run_zmap "32755,17007,4899"
sleep 21m

run_zmap "60004,1574,1068"
sleep 21m

run_zmap "32211,3632,19150"
sleep 21m

run_zmap "1467,1666,31416"
sleep 21m

run_zmap "9481,22490,1763"
sleep 21m

run_zmap "32780,32753,4369"
sleep 21m

run_zmap "5323,11210,13783"
sleep 21m

run_zmap "27003,427,1550"
sleep 21m

run_zmap "32763,1688,27010"
sleep 21m

run_zmap "628,616,37435"
sleep 21m

run_zmap "32807,8333,32762"
sleep 21m

run_zmap "60003,27002,32756"
sleep 21m

run_zmap "13720,1432,5302"
sleep 21m

run_zmap "27009,14238,510"
sleep 21m

run_zmap "524,30444,27005"
sleep 21m

run_zmap "1762,26214,32782"
sleep 21m

run_zmap "26470,32754,7461"
sleep 21m

run_zmap "710,50006,1549"
sleep 21m

run_zmap "27006,60010,32766"
sleep 21m

run_zmap "32781,50023,27007"
sleep 21m

run_zmap "32803,3493,50008"
sleep 21m

run_zmap "60007,60006,32759"
sleep 21m

run_zmap "32751,32784,32758"
sleep 21m

run_zmap "32760,32761,32783"
sleep 21m

run_zmap "32750,50007,3892"
sleep 21m

run_zmap "50021,50010,4868"
sleep 21m

run_zmap "50012,50011,50017"
sleep 21m

run_zmap "32786,60012,60020"
sleep 21m

run_zmap "60025,214,35"
sleep 21m

run_zmap "50009,44,32785"
sleep 21m

run_zmap "32800,60013,50016"
sleep 21m

run_zmap "60024,60011,50014"
sleep 21m

run_zmap "60015,50018,711"
sleep 21m

run_zmap "50020,60008,50004"
sleep 21m

run_zmap "50019,41523,32789"
sleep 21m

run_zmap "50024,60017,50013"
sleep 21m

run_zmap "60018,60016,60014"
sleep 21m

run_zmap "32788,32792,32793"
sleep 21m

run_zmap "32794,32790,32801"
sleep 21m

run_zmap "34012,782,32791"
sleep 21m

run_zmap "32804,56667,390"
sleep 21m

run_zmap "32805,32799,55553"
sleep 21m

run_zmap "32802,33015,1687"
sleep 21m

run_zmap "32806,731,130"
sleep 21m

run_zmap "32798,32809,660"
sleep 21m

run_zmap "32796,32810,706"
sleep 21m

run_zmap "32808,32795,38978"
sleep 21m

