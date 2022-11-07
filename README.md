# A prototype library benchmarker for Python Discord Libraries 
Please note, this project is in its infancy, and should not be relied on as a comparison tool yet

### Output
import:: Testing import times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 212.37ms         | 424.731µs          | 101.82%      |
| hata                 | DNF              | DNF                | DNF          |
| hikari               | 205.32ms         | 410.641µs          | 95.13%       |
| 🎉interactions.py    | 105.22ms         | 210.448µs          | 0.00%        |
| NAFF[perf]           | 360.36ms         | 720.719µs          | 242.47%      |

init:: Testing init times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 128.20ms         | 256.399µs          | 1016.69%     |
| 🎉hata               | 11.48ms          | 22.961µs           | 0.00%        |
| hikari               | 2818.36ms        | 5636.727µs         | 24449.56%    |
| interactions.py      | 167.23ms         | 334.459µs          | 1356.66%     |
| NAFF[perf]           | 90.18ms          | 180.358µs          | 685.51%      |

message:: Testing message deserialization times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 5.72ms           | 11.435µs           | 40.95%       |
| hata                 | 5.01ms           | 10.026µs           | 23.57%       |
| 🎉hikari             | 4.06ms           | 8.113µs            | 0.00%        |
| interactions.py      | 14.58ms          | 29.165µs           | 259.48%      |
| NAFF[perf]           | 9.47ms           | 18.949µs           | 133.56%      |

message_hard:: Testing message deserialization times for 500 iterations
| Library                | Total Time(ms)   | Average Time(µs)   | Difference   |
|------------------------|------------------|--------------------|--------------|
| 🎉discord.py[commands] | 28.45ms          | 56.904µs           | 0.00%        |
| hata                   | 48.33ms          | 96.654µs           | 69.86%       |
| hikari                 | 50.51ms          | 101.028µs          | 77.54%       |
| interactions.py        | 675.40ms         | 1350.801µs         | 2273.83%     |
| NAFF[perf]             | 154.65ms         | 309.301µs          | 443.55%      |

guild:: Testing guild deserialization times for 500 iterations
| Library              | Total Time(ms)   | Average Time(µs)   | Difference   |
|----------------------|------------------|--------------------|--------------|
| discord.py[commands] | 29.99ms          | 59.983µs           | 22.81%       |
| hata                 | DNF              | DNF                | DNF          |
| hikari               | 45.07ms          | 90.132µs           | 84.54%       |
| interactions.py      | 142.49ms         | 284.971µs          | 483.47%      |
| 🎉NAFF[perf]         | 24.42ms          | 48.841µs           | 0.00%        |
