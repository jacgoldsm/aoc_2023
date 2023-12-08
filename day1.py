with open("day1.txt", 'r') as f:
    text = f.read().split("\n")

acc = 0

import re
for line in text:
   start = re.findall(r"1|one|2|two|3|three|4|four|5|five|6|six|7|seven|8|eight|9|nine", line)[0]
   end  = re.findall(r"1|eno|2|owt|3|eerht|4|ruof|5|evif|6|xis|7|neves|8|thgie|9|enin", "".join(reversed(line)))[0]
   start = start.replace("one","1").replace("two","2").replace("three","3").replace("four","4").replace("five","5").replace("six","6").replace("seven","7").replace("eight","8").replace("nine","9")
   end = end.replace("eno","1").replace("owt","2").replace("eerht","3").replace("ruof","4").replace("evif","5").replace("xis","6").replace("neves","7").replace("thgie","8").replace("enin","9")
   print(f"{start} {end}")

   val = int(f"{start}{end}")
   acc += val

print(acc)
    