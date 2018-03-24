-- MySQL dump 10.13  Distrib 5.6.26, for Win64 (x86_64)
--
-- Host: localhost    Database: blogdb
-- ------------------------------------------------------
-- Server version	5.6.26-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `abstract` varchar(200) NOT NULL,
  `content` text NOT NULL,
  `uid` int(10) unsigned DEFAULT NULL,
  `pcount` int(10) unsigned DEFAULT '0',
  `flag` tinyint(3) unsigned DEFAULT '0',
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'番茄炒鸡蛋的做法','番茄炒鸡蛋','制作材料\n主料：番茄500克,鸡蛋200克\n番茄\n番茄(16张)\n调料：植物油80克,白砂糖100克,淀粉(豌豆)5克[1]\n特色\n红黄相间，鲜香酸甜。\n制作流程\n1、把西红柿洗净，去蒂，切成象眼块;\n2、鸡蛋打入碗内，加入盐少许，搅匀;\n3、将炒锅放植物油，先将鸡蛋倒入，炒成散块，盛出;\n4、炒锅中再少放些植物油，油烧热后放入西红柿翻炒几下，再放入鸡蛋，搅炒均匀加入白糖、盐，再翻炒几下，用淀粉勾芡即成。',1,23,1,'2018-04-05 00:00:00'),(2,'BP神经网络梯度下降算法','菜鸟初学人智相关问题，智商低，艰苦学习中，转文只为保存，其中加上了一些个人注释，便于更简单的理解~新手也可以看，共勉','第一区域的来说，它们相当于外界的刺激，是刺激的来源并且将刺激传递给神经元，因此把第一区域命名为输入层。第二区域，表示神经元相互之间传递刺激相当于人脑里面，因此把第二区命名为隐藏层。第三区域，表示神经元经过多层次相互传递后对外界的反应，因此把第三区域命名为输出层。\n 简单的描述就是，输入层将刺激传递给隐藏层，隐藏层通过神经元之间联系的强度（权重）和传递规则（激活函数）将刺激传到输出层，输出层整理隐藏层处理的后的刺激产生最终结果。若有正确的结果，那么将正确的结果和产生的结果进行比较，得到误差，再逆推对神经网中的链接权重进行反馈修正，从而来完成学习的过程。这就是BP神经网的反馈机制，也正是BP（Back  Propagation）名字的来源：运用向后反馈的学习机制，来修正神经网中的权重，最终达到输出正确结果的目的！。',1,52,1,'2018-04-10 00:00:00'),(3,'牛顿迭代法求解开方问题','求解开方问题','以方程 x2=nx2=n 为例，\n令 f(x)=x2−nf(x)=x2−n，也就是相当于求解 f(x)=0f(x)=0 的解。，即可求出： \n',2,13,1,'2018-04-10 00:00:00'),(4,'自动驾驶语义分割模型','Deep Learning Architectures','In a previous post, we studied various open datasets that could be used to train a model for pixel-wise semantic segmentation of urban scenes. Here, we take a look at various deep learning architectures that cater specifically to time-sensitive domains like autonomous vehicles. In recent years, deep learning has surpassed traditional computer vision algorithms by learning a hierarchy of features from the training dataset itself. This eliminates the need for hand-crafted features and thus such techniques are being extensively explored in academia and industry.',3,25,1,'2018-04-12 00:00:00'),(5,'tensorflow队列读取机制','tensorflow提供了三种读取数据的机制，分别是1.constant, 2.feed_dict ,3. file reader。','对于数据读取一般会有这两个问题：1.内存占用 2.数据读取时间。对于较大的数据集，由于内存限制，feed方式直接把全部数据加载到内存中是不可能的，\ntf.train.batch(\ntensors,\nbatch_size,\nnum_threads=1,\ncapacity=32\n)其中，capcity是样本队列的容量，num_thread是reader的读取线程，如果超过1，会进行单reader多线程读取。当进行多线程读取时，队列会将数据均匀的分给不同的线程，最大程度的提高速度。由于是并行的所以数据会被打乱，如果想要更shuffle的效果，可以使用shuffle_batch，每次出队时数据会被shuffle一次，但是这个函数要注意设置capcity，已提供足够的空间执行shuffle操作',4,22,1,'2018-04-16 00:00:00'),(6,'监督学习和无监督学习的区别','监督学习和无监督学习的区别','机器学习的常用方法，主要分为有监督学习(supervised learning)和无监督学习(unsupervised learning)。监督学习，就是人们常说的分类，通过已有的训练样本（即已知数据以及其对应的输出）去训练得到一个最优模型（这个模型属于某个函数的集合，最优则表示在某个评价准则下是最佳的），再利用这个模型将所有的输入映射为相应的输出，对输出进行简单的判断从而实现分类的目的，也就具有了对未知数据进行分类的能力。在人对事物的认识中，我们从孩子开始就被大人们教授这是鸟啊、那是猪啊、那是房子啊，等等。我们所见到的景物就是输入数据，而大人们对这些景物的判断结果（是房子还是鸟啊）就是相应的输出。当我们见识多了以后，脑子里就慢慢地得到了一些泛化的模型，这就是训练得到的那个（或者那些）函数，从而不需要大人在旁边指点的时候，我们也能分辨的出来哪些是房子，哪些是鸟。',4,13,1,'2018-04-16 00:00:00'),(7,'测试标题1','用于测试1','测试内容1啊',5,1,0,'2018-04-16 00:00:00'),(8,'测试标题2','用于测试2','测试内容2啊',6,2,2,'2018-04-16 00:00:00'),(9,'测试标题3','用于测试3','测试内容3啊',7,12,1,'2018-04-10 00:00:00'),(10,'测试标题4','用于测试4','测试内容4啊',8,19,1,'2018-04-11 00:00:00'),(11,'测试标题5','用于测试5','测试内容5啊',9,8,1,'2018-04-11 00:00:00'),(12,'测试标题6','用于测试6','测试内容6啊',10,15,1,'2018-04-20 00:00:00');
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'用户1','aa1@163.com','2018-03-15 00:00:00'),(2,'用户2','aa2@163.com','2018-03-15 00:00:00'),(3,'用户3','aa3@163.com','2018-03-15 00:00:00'),(4,'用户4','aa4@163.com','2018-03-16 00:00:00'),(5,'用户5','aa5@163.com','2018-03-16 00:00:00'),(6,'用户6','aa6@163.com','2018-03-16 00:00:00'),(7,'用户7','aa7@163.com','2018-03-17 00:00:00'),(8,'用户8','aa8@163.com','2018-03-17 00:00:00'),(9,'用户9','aa9@163.com','2018-03-18 00:00:00'),(10,'用户10','aa10@163.com','2018-03-18 00:00:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-24 11:32:17
