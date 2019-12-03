### HTTP Log monitoring console programs that monitors HTTP traffic on your machine

The idea is this program actively consumes an active http log and
output some interesting information and sound alarm.

The result is two programs, one from part 0, the other from part I and
II. You keep them running at the same time.

It's a classic consumer/producer problem. Part 0 and Part I can be
done onsite in about an hour. I have boiler plate program. They just
need to fill 2-3 functions. Part II can be take home.

#### Part 0 Create/Fake an active http log

Write a program to create an actively written-to w3c-formatted HTTP access log
Active http log means, a file keeps getting new record at Random second.

#### Part I Gathering interesting information

Every 10s, display in the console the sections of the web site with
the most hits (a section is defined as being what's before the second
'/' in a URL. i.e. the section for "http://my.site.com/pages/create'
is "http://my.site.com/pages"), as well as interesting summary
statistics on the traffic as a whole.

#### Part II alarm

a) Whenever total traffic for the past 2 minutes exceeds a certain
number on average, add a message saying that “High traffic generated
an alert - hits = {value}, triggered at {time}”

b) Whenever the total traffic drops again below that value on average
for the past 2 minutes, add another message detailing when the alert
recovered

Make sure all messages showing when alerting thresholds are crossed
remain visible on the page for historical reasons.

Write a test for the alerting logic Explain how you’d improve on this
application design
