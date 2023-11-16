
## Abstract

- In Assignment 2, I implemented **BOLA-BASIC** (Buffer Occupancy based Lyapunov Algorithm) after reading the article, “BOLA: Near-Optimal Bitrate Adaptation for Online Videos”.
- This article formulates bitrate adaptation as a utility maximization problem that incorporates both key components of QoE(Quality of Experience): the average bitrate of the video experienced by the user and the duration of the rebuffer events. An increase in the average bitrate will increase utility, whereas rebuffering will decrease it. 


- Using Lyapunov optimization, it derives an online bitrate adaptation algorithm called BOLA that achieves utility which is within an additive factor of the maximum possible utility. This algorithm is the first to provide a theoretical guarantee on the achieved utility. 

- The pseudocode is as below:


  <img width="233" alt="image" src="https://github.com/Yifu-Tian/ECE4016/assets/102942951/3d9838bc-b001-4ba4-89c7-51c28f3548f4">
