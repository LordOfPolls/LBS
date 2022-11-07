# A prototype library benchmarker for Python Discord Libraries 
Please note, this project is in its infancy, and should not be relied on as a comparison tool yet

### Output
```
import:: Testing import times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 51.03ms          | 102.063µs          | 5062.51%     |
| hata                 | DNF              | DNF                | DNF          |
| 🎉hikari             | 0.99ms           | 1.977µs            | 0.00%        |
| interactions.py      | 103.17ms         | 206.344µs          | 10337.22%    |
| NAFF[perf]           | 359.60ms         | 719.192µs          | 36277.93%    |

init:: Testing init times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 128.84ms         | 257.684µs          | 1025.43%     |
| 🎉hata               | 11.45ms          | 22.896µs           | 0.00%        |
| hikari               | 2909.48ms        | 5818.967µs         | 25314.33%    |
| interactions.py      | 192.69ms         | 385.372µs          | 1583.11%     |
| NAFF[perf]           | 90.73ms          | 181.454µs          | 692.50%      |

message:: Testing message deserialization times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 6.02ms           | 12.037µs           | 45.56%       |
| hata                 | 5.31ms           | 10.611µs           | 28.31%       |
| 🎉hikari             | 4.13ms           | 8.270µs            | 0.00%        |
| interactions.py      | 14.81ms          | 29.614µs           | 258.08%      |
| NAFF[perf]           | 9.31ms           | 18.614µs           | 125.08%      |

message_hard:: Testing message deserialization times for 500 iterations
| Library                | Total Time(ms)   | Average Time(µs)   | Difference   |
|------------------------|------------------|--------------------|--------------|
| 🎉discord.py[commands] | 28.22ms          | 56.438µs           | 0.00%        |
| hata                   | 48.80ms          | 97.597µs           | 72.93%       |
| hikari                 | 58.79ms          | 117.587µs          | 108.35%      |
| interactions.py        | 685.49ms         | 1370.987µs         | 2329.18%     |
| NAFF[perf]             | 132.29ms         | 264.585µs          | 368.80%      |

guild:: Testing guild deserialization times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 28.49ms          | 56.981µs           | 12.75%       |
| hata                 | DNF              | DNF                | DNF          |
| hikari               | 39.13ms          | 78.255µs           | 54.85%       |
| interactions.py      | 150.64ms         | 301.277µs          | 496.15%      |
| 🎉NAFF[perf]         | 25.27ms          | 50.537µs           | 0.00%        |
