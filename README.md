# hellow-world<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>作业模板1</title>
	<style type="text/css">
        *{padding:0;margin:0;}
        /*body{background-image:url(img/6.jpg);}*/
        .header ul{width:1000px;height:50px;margin:0 auto;padding:0;background-color:rgb(175,14,55);}
        .header ul li{list-style-type:none;float:left;}
        .header ul li a{display:block;width:200px;line-height:50px;text-align:center;text-decoration:none;color:white;}
        .jpg{margin:0 auto;width:1000px;height:180px;}
        .jpg img{width:1000px;height:180px;}
        .main{width:1000px;height:auto;margin:0 auto;}
        .main .left{width:70%;height:150px;float:left;margin:10px 0 60px 0;}
        .main .right{width:28%;height:150px;float:right;margin:10px 0 60px 0;}
        .main .bottom{width:100%;height:auto;clear:both;}
        .footer{width:1000px;margin:60px auto;}
	</style>
</head>
<body>
	<div class="header">
       <ul>
       	<li><a href="index.html">站点首页</a></li>
        <li><a href="lishi.html">中国女排</a></li>
        <li><a href="shipin.html">精彩视频</a></li>
       </ul>
       <div class="jpg">
       <img src="img/01.jpg" alt="这是图片">
       </div>
	</div>
	<div class="main">
        <div class="left">
             <p style="background-color:rgb(175,14,55);padding:5px 0 5px 15px;color:white;">中国女排</p>
             <p style="padding:10px;background-color:#FFFFFF;height:100%;">中国国家女子排球队（简称中国女排）隶属于中国排球协会，是中国各体育团队中成绩突出的体育团队之一。曾在1981年和1985年世界杯、1982年和1986年世锦赛、1984年洛杉矶奥运会上夺得冠军，成为世界上第一个“五连冠”，并又在2003年世界杯、2004年奥运会、2015年世界杯、2016年奥运会、2019年世界杯五度夺冠，共十度成为世界冠军（包括世界杯、世锦赛和奥运会三大赛）。 中国女排是中国三大球中唯一一个拿到冠军奖杯的队伍。</p>
        </div>
        <div class="right">
             <p style="background-color:rgb(175,14,55);padding:5px 0 5px 15px;color:white;">女排视频</p>
             <p style="padding:10px;background-color:#FFFFFF;height:100%;">
               <video controls="controls" style="width:100%;">
                   <source src="video\01.mp4">
                 <!-- Your browser does not support the video tag. -->
               </video>
             </p>
        </div>

         <div class="bottom">
            <p style="background-color:rgb(175,14,55);padding:5px 0 5px 15px;color:white;">队员图片</p>
            <p  style="background-color:#FFFFFF; padding-bottom:15px;">
               <img src="img/1.jpg" width="236" height="200" alt=""  style="margin-top:10px;">
               <img src="img/2.jpg" width="236" height="200" alt="" style="margin-left:12px;">
               <img src="img/3.jpg" width="236" height="200" alt="" style="margin-left:12px;">
               <img src="img/4.jpg" width="236" height="200" alt="" style="margin-left:12px;">
               <img src="img/5.jpg" width="236" height="200" alt="" style="margin-top:10px;">
               <img src="img/6.jpg" width="236" height="200" alt="" style="margin-top:10px;margin-left:12px;">
               <img src="img/7.jpg" width="236" height="200" alt="" style="margin-top:10px;margin-left:12px;">
               <img src="img/8.jpg" width="236" height="200" alt="" style="margin-top:10px;margin-left:12px;">
            </p>
        </div>
	</div>
       
	<div class="footer">
      <p style="text-align:center;padding:10px;background-color:rgb(175,14,55);color:white;">版权所有，翻版必究</p>
  </div>
</body>
</html>
