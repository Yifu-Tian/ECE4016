# Abstract

- In Assignment 2, I implemented **BOLA-BASIC** (Buffer Occupancy based Lyapunov Algorithm) after reading the article, “BOLA: Near-Optimal Bitrate Adaptation for Online Videos”.
- This article formulates bitrate adaptation as a utility maximization problem that incorporates both key components of QoE(Quality of Experience): the average bitrate of the video experienced by the user and the duration of the rebuffer events. An increase in the average bitrate will increase utility, whereas rebuffering will decrease it. 


- Using Lyapunov optimization, it derives an online bitrate adaptation algorithm called BOLA that achieves utility which is within an additive factor of the maximum possible utility. This algorithm is the first to provide a theoretical guarantee on the achieved utility. 

# Test & Evaluation

<img width="300" alt="image" src="https://github.com/Yifu-Tian/ECE4016/assets/102942951/eb7dba17-258e-41a8-beb6-89ff6017cfdc">
<img width="296" alt="image" src="https://github.com/Yifu-Tian/ECE4016/assets/102942951/6e700bbe-7c64-4a10-8ea1-b0f30f12d949">

The evaluation of BOLA-BASIC is centered around its performance in achieving a balance between video quality and the possibility of rebuffering events. 

1.The algorithm assigns utility values to different bitrates based on the logarithmic function, which inherently values a smooth playback experience instead of aggressive quality maximization. The utility-based approach ensures that the quality of the video adapts dynamically, ensuring that the viewer's experience is optimized within the constraints of the current buffer state.

2.In terms of performance metrics, BOLA-BASIC’s effectiveness is demonstrated through comparisons with the offline optimal bound and other adaptive bitrate algorithms. The comparisons highlight BOLA-BASIC’s strength in maintaining a high utility value while minimizing rebuffering events, which is a critical aspect of the viewer's quality of experience.

3.The adaptability of BOLA-BASIC is particularly notable. It shows resilience to fluctuating network conditions and reacts solely based on buffer thresholds, which eliminates the need for complex bandwidth prediction mechanisms. This buffer-only decision-making process simplifies the algorithm's implementation while still delivering a robust streaming experience.

4.BOLA-BASIC also showcases its efficacy through simulations that reveal its competence in handling various network profiles and video lengths. Its utility values remain consistently close to the optimal, signifying that it can effectively maximize the perceived quality of the video content across different scenarios.

5.Furthermore, the BOLA-BASIC algorithm is easy to tune with a single parameter, V, which adjusts the trade-off between bitrate and buffer occupancy. By tuning V, providers can customize the aggressiveness of bitrate selection to cater to specific content or network environments.
