Read hour markings from stdin and produce aggregated hour statistics per comment item.

Input format:

    hh:mm:ss<tab>Comment

where &lt;tab> represents the tab character (ASCII 9). Comment: one or more items, separated from each other by commas or semicolons.

Sample input:

    01:30:00<tab>Thing1, thing2
    04:00:00<tab>Thing2, thing3

Sample output:

    0.75<tab>Thing1
    2.75<tab>Thing2
    2.0<tab>Thing3
