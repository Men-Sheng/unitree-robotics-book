# 宇树 G1 拆解视频 - 事实核查清单

## 已确认的技术参数（来源已标注）

### 基本参数
- **高度**: 1.34m（站立）/ 0.69m（折叠）
- **重量**: 约 35kg（含电池）
- **自由度**: 25 DOF（G1+标准版）
- **关节电机数**: 23-43 个（根据配置）

来源: [Unitree 官网 G1+](https://www.unitree.com/G1plus/), [Weston Robot 文档](https://docs.westonrobot.com/tutorial/unitree/g1_dev_guide)

### 关节配置
- **头部**: 2 DOF（俯仰 -25°~36°，偏航 ±110°）
- **单腿**: 6 DOF
  - 膝关节: 0~165°
  - 髋关节: P±154°、R-30~+170°、Y±158°
- **腰部**: 1 DOF（标准）/ 3 DOF（可选）
- **单臂**: 5 DOF
- **臂展**: 约 0.45m
- **腿长**: 大腿+小腿 0.6m
- **手臂最大负载**: 3kg（G1+）/ 4kg（G1+ EDU）

来源: [Unitree 官网 G1+](https://www.unitree.com/G1plus/)

### 电机系统
- **电机类型**: 低惯量高速内转子永磁同步电机（PMSM）
- **轴承**: 工业级交叉滚子轴承（高精度、高负载能力）
- **编码器**: 双编码器系统
- **冷却**: 局部风冷
- **性能提升**（相比前代）:
  - 肩部和腰部电机峰值扭矩 +110%，同扭矩发热 -72%
  - 手臂电机峰值扭矩 +43%，同扭矩发热 -30%
  - 大腿电机同扭矩发热 -28%

来源: [Unitree 官网 G1+](https://www.unitree.com/G1plus/), [Motor Watt 评测](https://motorwatt.com/community/community-groups/humanoids-of-the-future-humanoid-robots/videos/unitree-g1-humanoid-robot-review-and-price)

### 控制系统
- **CPU**: 8 核高性能处理器
- **可选算力**: 支持 Orin 等多品牌高算力模块
- **通信**: WiFi 6, Bluetooth 5.2
- **OTA 升级**: 支持智能 OTA

来源: [Unitree 官网 G1+](https://www.unitree.com/G1plus/)

### 感知系统
- **双目相机**: 间距 60mm，200 万像素，中心≥500LW/PH，FOV H110°/V80°/D125°
- **广角单目**: 1920×1080@30fps，FOV H117°/V67°
- **3D 激光雷达**: 有（具体型号未公开）
- **麦克风**: 6 麦阵列（前 4 后 2），支持 DOA 声源定位
- **扬声器**: 腰部双 10W 扬声器
- **触摸传感器**: 头部集成

来源: [Unitree 官网 G1+](https://www.unitree.com/G1plus/)

### 电源系统
- **电池**: 13 串锂电池，9000mAh
- **续航**: 约 2 小时
- **充电器**: 54V 5A
- **外部供电**: 支持持续供电

来源: [Unitree 官网 G1+](https://www.unitree.com/G1plus/)

## 需要确认的内容

### 1. 核心信息语句
**建议**: "宇树重新定义了四足机器人的运动极限"
**问题**: G1 是**人形机器人**，不是四足机器人（四足是 Go 系列）

**修改建议**:
- "宇树 G1：重新定义人形机器人的运动极限"
- "宇树让机器人从实验室走进现实世界"
- "高性能人形机器人的平价革命"

### 2. 未公开的技术细节
以下内容在公开资料中未找到具体数值，视频中将用抽象可视化替代：
- 电机具体峰值扭矩数值（N·m）
- 关节最大角速度（°/s）
- 激光雷达具体型号和参数
- 控制系统架构图（专有技术）
- 具体的电路板布局

### 3. 视觉表现策略
由于无法获得 G1 实物照片或 3D 模型，所有画面将使用：
- 几何线框表示结构
- 粒子系统表示运动和能量
- 抽象图形表示技术原理
- 数据可视化表示参数

## 引用来源

1. Unitree 官网 G1+ 页面: https://www.unitree.com/G1plus/
2. Weston Robot G1 开发指南: https://docs.westonrobot.com/tutorial/unitree/g1_dev_guide
3. Wikipedia - Unitree Robotics: https://en.wikipedia.org/wiki/Unitree_Robotics
4. Motor Watt G1 评测: https://motorwatt.com/community/community-groups/humanoids-of-the-future-humanoid-robots/videos/unitree-g1-humanoid-robot-review-and-price

## 风险提示

1. **品牌敏感**: 宇树科技是真实公司，视频内容必须基于公开事实，不能编造技术参数
2. **专利风险**: 控制算法、电机设计等核心技术为商业机密，只能展示公开信息
3. **竞品对比**: 避免与 Boston Dynamics、Tesla 等竞品直接对比
4. **性能承诺**: 不夸大性能，不暗示未公开的功能