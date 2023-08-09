<html lang="en">

<head>
    <title>Register</title>
    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
<style>
.header {	position: relative;
			top:0;	
			margin:0px;
			z-index: 1;
			left: 0px;
			right: 0px;
			position: fixed;
			background-color: #F36262 ;
			color: white;
			box-shadow: 0px 8px 4px grey;
			overflow: hidden;
			padding-left:20px;
			font-family: 'Josefin Sans';
			font-size: 2vw;
			width: 100%;
			height:8%;
			text-align: center;
		}
		.topnav {
  overflow: hidden;
  background-color: #FCAD98;
}

.topnav-right a {
  float: left;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 18px;
}

.topnav-right a:hover {
  background-color: #FCAD98;
  color: black;
}

.topnav-right a.active {
  background-color: #FCAD98;
  color: white;
}

.topnav-right {
  float: right;
  padding-right:100px;
}

body {

  background-color: ;
  background-repeat: no-repeat;
  background-size:cover;
  background-image: url("https://i.pinimg.com/originals/b2/1d/c6/b21dc69346915015bc4e19bd502f401b.gif");
    background-size: cover;
  background-position: 0px 0px;
  }
  .button {
  background-color: #091425; 
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  border-radius: 16px;
}
.button:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
form {border: 3px solid #f1f1f1; margin-left:400px;margin-right:400px;}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  display: inline-block;
  margin-bottom:18px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #091425;
  color: white;
  padding: 14px 20px;
  margin-bottom:10px;
  border: none;
  cursor: pointer;
  width: 17%;
  border-radius:4px;
  font-family:Montserrat;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 30%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}

.home{
	margin:80px;
	
  width: 84%;
  height: 500px;
  padding-top:10px;
  padding-left: 30px;  
  
}
.login{
	margin:80px;
	box-sizing: content-box;  
  width: 84%;
  height: 420px;
  padding: 30px;  
  border: 10px solid blue;
}
.left,.right{
 box-sizing: content-box; 
 height: 400px;
 margin:20px;
 border: 10px solid blue;
}

.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #FCAD98;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}








.bar
{
margin: 0px;
padding:20px;
background-color:white;
opacity:0.6;
color:black;
font-family:'Roboto',sans-serif;
font-style: italic;
border-radius:20px;
font-size:25px;
}
a
{
color:grey;
float:right;
text-decoration:none;
font-style:normal;
padding-right:20px;
}
a:hover{
background-color:black;
color:white;
border-radius:15px;0
font-size:30px;
padding-left:10px;
}
body
{
    background-image: url("https://images.unsplash.com/photo-1532883130016-f3d311140ba8?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80");
    background-size: cover;
}
p
{
color:white;
font-style:italic;
font-size:30px;
}
</style> 
</head>

<body>

<div class="header">    
<div style="width:50%;float:left;font-size:2vw;text-align:left;color:black; padding-top:1%;padding-left:5%;">AI based Natural disaster analysis</div>
  <div class="topnav-right"style="padding-top:0.5%;">
    
    <a  href="/home">Home</a>
    <a href="/intro">Introduction</a>
    <a class="active" href="/upload">Open Web Cam</a>
  </div>
</div>

</body>

<html>
<script>


</script>


<style>
.header {	position: relative;
			top:0;	
			margin:0px;
			z-index: 1;
			left: 0px;
			right: 0px;
			position: fixed;
			background-color: rgba(100, 100, 100, 0.5) ;
			color: white;
			box-shadow: 0px 8px 4px grey;
			overflow: hidden;
			padding-left:20px;
			font-family: 'Josefin Sans';
			font-size: 2vw;
			width: 100%;
			height:8%;
			text-align: center;
		}
		.topnav {
  overflow: hidden;
  background-color: #FCAD98;
}

.topnav-right a {
  float: left;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 18px;
}

.topnav-right a:hover {
  background-color: #FCAD98;
  color: black;
}

.topnav-right a.active {
  background-color: #FCAD98;
  color: white;
}

.topnav-right {
  float: right;
  padding-right:100px;
}

body {

  background-color: ;
  background-repeat: no-repeat;
  background-size:cover;
  
    background-size: cover;
  background-position: 0px 0px;
  }
  .button {
  background-color: #091425; 
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  border-radius: 16px;
}
.button:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
form {border: 3px solid #f1f1f1; margin-left:400px;margin-right:400px;}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  display: inline-block;
  margin-bottom:18px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #091425;
  color: white;
  padding: 14px 20px;
  margin-bottom:10px;
  border: none;
  cursor: pointer;
  width: 17%;
  border-radius:4px;
  font-family:Montserrat;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 30%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}

.home{
	margin:80px;
	
  width: 84%;
  height: 500px;
  padding-top:10px;
  padding-left: 30px;  
  
}
.login{
	margin:80px;
	box-sizing: content-box;  
  width: 84%;
  height: 420px;
  padding: 30px;  
  border: 10px solid blue;
}
.left,.right{
 box-sizing: content-box; 
 height: 400px;
 margin:20px;
 border: 10px solid blue;
}

.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #FCAD98;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}



@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");

* {
  padding: 0;
  margin: 0;
}

body {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-family: "Montserrat Medium";
  max-width: 90ch;
  text-align: center;
  transform: scale(0.94);
  animation: scale 3s forwards cubic-bezier(0.5, 1, 0.89, 1);
}
@keyframes scale {
  100% {
    transform: scale(1);
  }
}

span {
  display: inline-block;
  opacity: 0;
  filter: blur(4px);
}

span:nth-child(1) {
  animation: fade-in 1s 0.1s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(2) {
  animation: fade-in 0.8s 0.2s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(3) {
  animation: fade-in 0.8s 0.3s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(4) {
  animation: fade-in 0.8s 0.4s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(5) {
  animation: fade-in 0.8s 0.5s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(6) {
  animation: fade-in 0.8s 0.6s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(7) {
  animation: fade-in 0.8s 0.7s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(8) {
  animation: fade-in 0.8s 0.8s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(9) {
  animation: fade-in 0.8s 0.9s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(10) {
  animation: fade-in 0.8s 1s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(11) {
  animation: fade-in 0.8s 1.1s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(12) {
  animation: fade-in 0.8s 1.2s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(13) {
  animation: fade-in 0.8s 1.3s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(14) {
  animation: fade-in 0.8s 1.4s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(15) {
  animation: fade-in 0.8s 1.5s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(16) {
  animation: fade-in 0.8s 1.6s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(17) {
  animation: fade-in 0.8s 1.7s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

span:nth-child(18) {
  animation: fade-in 0.8s 1.8s forwards cubic-bezier(0.11, 0, 0.5, 0);
}
span:nth-child(19) {
  animation: fade-in 0.8s 1.9s forwards cubic-bezier(0.11, 0, 0.5, 0);
}
span:nth-child(20) {
  animation: fade-in 0.8s 2.0s forwards cubic-bezier(0.11, 0, 0.5, 0);
}
span:nth-child(21) {
  animation: fade-in 0.8s 2.1s forwards cubic-bezier(0.11, 0, 0.5, 0);
}
span:nth-child(22) {
  animation: fade-in 0.8s 2.2s forwards cubic-bezier(0.11, 0, 0.5, 0);
}
span:nth-child(23) {
  animation: fade-in 0.8s 2.3s forwards cubic-bezier(0.11, 0, 0.5, 0);
}span:nth-child(24) {
  animation: fade-in 0.8s 2.4s forwards cubic-bezier(0.11, 0, 0.5, 0);
}span:nth-child(25) {
  animation: fade-in 0.8s 2.5s forwards cubic-bezier(0.11, 0, 0.5, 0);
}span:nth-child(26) {
  animation: fade-in 0.8s 2.6s forwards cubic-bezier(0.11, 0, 0.5, 0);
}span:nth-child(27) {
  animation: fade-in 0.8s 2.7s forwards cubic-bezier(0.11, 0, 0.5, 0);
}span:nth-child(28) {
  animation: fade-in 0.8s 2.8s forwards cubic-bezier(0.11, 0, 0.5, 0);
}
@keyframes fade-in {
  100% {
    opacity: 1;
    filter: blur(0);
  }
}

</style>

<body>
<h1>
  <span> China, India and the United States </span> <span> are among the countries of the world most </span> <span> affected by natural disasters. </span > <span> Natural disasters have the potential to wreck and even end the lives of those people,</span> <span>who stand in their way.</span> <span>  However, whether or not you are likely to be  </span> <span> affected by a natural disaster greatly depends</span > <span>  on where in the world you live, </span>
  <span> The objective of </span> <span> the project is to</span> <span>human build a </span > <span> web application </span> <span> to detect the </span> <span> type of disaster .</span> <span> The input </span > <span> is taken from the in built web cam,</span>
<span> which in turn </span> <span> is </span> <span> given to the  </span > <span>pre trained model .</span> <span> The model predicts the  </span> <span> type of disaster </span> <span> and displayed</span > <span> on UI.</span>


</h1>
<!--Brian Tracy-->

<div class="header">    
<div style="width:50%;float:left;font-size:2vw;text-align:left;color:black; padding-top:1%;padding-left:5%;">AI based Natural disaster analysis</div>
  <div class="topnav-right"style="padding-top:0.5%;">
    
    <a  href="/home">Home</a>
    <a class="active" href="/intro">Introduction</a>
    <a href="/upload">Open Web Cam</a>
  </div>
</div>
</body>

</html>

<html>
<script>
        
</script>

<style>
.header {	position: relative;
			top:0;	
			margin:0px;
			z-index: 1;
			left: 0px;
			right: 0px;
			position: fixed;
			background-color: #FCAD98 ;
			color: white;
			box-shadow: 0px 8px 2px grey;
			overflow: hidden;
			padding-left:20px;
			font-family: 'Josefin Sans';
			font-size: 2vw;
			width: 100%;
			height:8%;
			text-align: center;
		}
		.topnav {
  overflow: hidden;
  background-color: #FCAD98;
}

.topnav-right a {
  float: left;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 18px;
}

.topnav-right a:hover {
  background-color: #FCAD98;
  color: black;
}

.topnav-right a.active {
  background-color: #FCAD98;
  color: white;
}

.topnav-right {
  float: right;
  padding-right:100px;
}

body {
background-image: -webkit-linear-gradient(90deg, skyblue 0%, steelblue 100%);
  background-image: url("");
    background-size: cover;
  background-attachment: fixed;
  background-size: 100% 100%;
  background-color: ;
  background-repeat: no-repeat;
  background-size:cover;
  background-position: 0px 0px;
  }
  .button {
  background-color: #091425; 
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  border-radius: 16px;
}
.button:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
form {border: 3px solid #f1f1f1; margin-left:400px;margin-right:400px;}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  display: inline-block;
  margin-bottom:18px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #091425;
  color: white;
  padding: 14px 20px;
  margin-bottom:10px;
  border: none;
  cursor: pointer;
  width: 17%;
  border-radius:4px;
  font-family:Montserrat;
}

button:hover {
  opacity: 0.8;
}

.cancelbtn {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 30%;
  border-radius: 50%;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .cancelbtn {
     width: 100%;
  }
}

.home{
	margin:80px;
	
  width: 84%;
  height: 500px;
  padding-top:10px;
  padding-left: 30px;  
  
}
.login{
	margin:80px;
	box-sizing: content-box;  
  width: 84%;
  height: 420px;
  padding: 30px;  
  border: 10px solid blue;
}
.left,.right{
 box-sizing: content-box; 
 height: 400px;
 margin:20px;
 border: 10px solid blue;
}

.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #FCAD98;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}










@import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');

* {
  box-sizing: border-box;
}

body {
  min-height: 100vh;
  margin: 0;
  color: #fff;
  font-family: 'Poppins',sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5f5f5;
}

.container {
  max-width: 1376px;
  margin: auto;
  padding: 2rem 1.5rem;
}

.cards {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

.card {
  cursor: pointer;
  background-color: transparent;
  height: 300px;
  perspective: 1000px;
  margin: 1rem;
  align-items: center;
  justify-content: center;
}

.card h3 {
  border-bottom: 1px #fff solid;
  padding-bottom: 10px;
  margin-bottom: 10px;
  text-align: center;
  font-size: 1.6rem;
  word-spacing: 3px;
}

.card p{
  opacity: 0.75;
  font-size: 0.8rem;
  line-height: 1.4;
}

.card img {
  width: 360px;
  height: 300px;
  object-fit: cover;
  border-radius: 3px;
}

.card-inner {
  position: relative;
  width: 360px;
  height: 100%;
  transition: transform 0.9s;
  transform-style: preserve-3d;
}

.card:hover .card-inner {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  position: absolute;
  width: 360px;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.card-back {
  background-color: #222;
  color: #fff;
  padding: 1.5rem;
  transform: rotateY(180deg);
}
.text-block {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background-color: black;
  color: white;
  
  padding-left: 20px;
  padding-right: 20px;
}
</style>

<body>
<div class="header">    
<div style="width:50%;float:left;font-size:2vw;text-align:left;color:black; padding-top:1%;padding-left:5%;">AI based Natural disaster analysis</div>
  <div class="topnav-right"style="padding-top:0.5%;">
    
    <a class="active" href="/home">Home</a>
    <a href="/intro">Introduction</a>
    <a href="/upload">Open Web Cam</a>
  </div>
</div>



<div class="container">

        <div class="cards">

            <div class="card">
                <div class="card-inner">
                    <div class="card-front">
                        <img src="https://images.unsplash.com/photo-1454789476662-53eb23ba5907?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=689&q=80"
                            alt="">
<div class="text-block">
    <h2>Cyclone</h2>
    <p>violent winds, torrential rain, high waves and, very destructive storm</p>
  </div>

                    </div>
                    <div class="card-back">
                        <h3>Cyclone</h3>
                        <p>The effects of tropical cyclones include heavy rain, strong wind, large storm surges near landfall, and tornadoes. The destruction from a tropical cyclone, such as a hurricane or tropical storm, depends mainly on its intensity, its size, and its location.</p>
                    </div>
                </div>
            </div>


<div class="container">

        <div class="cards">

            <div class="card">
                <div class="card-inner">
                    <div class="card-front">
                        <img src="https://images.unsplash.com/photo-1603869311144-66b03d340b32?ixid=MXwxMjA3fDB8MHxzZWFyY2h8M3x8ZWFydGhxdWFrZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
                            alt="">
<div class="text-block">
    <h2>Earth Quake</h2>
    <p>Sudden release of stored energy in the Earth's crust that creates seismic waves.</p>
  </div>

                    </div>
                    <div class="card-back">
                        <h3>Earth Quake</h3>
                        <p>Earthquakes are usually caused when rock underground suddenly breaks along a fault. This sudden release of energy causes the seismic waves that make the ground shake. ... During the earthquake and afterward, the plates or blocks of rock start moving, and they continue to move until they get stuck again.</p>
                    </div>
                </div>
            </div>



<div class="container">

        <div class="cards">

            <div class="card">
                <div class="card-inner">
                    <div class="card-front">
                        <img src="https://images.unsplash.com/photo-1547683905-f686c993aae5?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8Zmxvb2R8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
                            alt="">
<div class="text-block">
    <h2>Flood</h2>
    <p>A flood is an overflow of water on normally dry ground</p>
  </div>

                    </div>
                    <div class="card-back">
                        <h3>Flood</h3>
                        <p>During heavy rain, the storm drains can become overwhelmed or plugged by debris and flood the roads and buildings nearby. Low spots, such as underpasses, underground parking garages, basements, and low water crossings can become death traps. Areas near rivers are at risk from floods.</p>
                    </div>
                </div>
            </div>



<div class="container">

        <div class="cards">

            <div class="card">
                <div class="card-inner">
                    <div class="card-front">
                        <img src="https://images.unsplash.com/photo-1473260079709-83c808703435?ixid=MXwxMjA3fDB8MHxzZWFyY2h8NHx8d2lsZGZpcmV8ZW58MHx8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"
                            alt="">
<div class="text-block">
    <h2>WildFire</h2>
    <p>Uncontrolled fire in a forest, grassland, brushland</p>
  </div>

                    </div>
                    <div class="card-back">
                        <h3>Wildfire</h3>
                        <p>Wildfires can be caused by an accumulation of dead matter (leaves, twigs, and trees) that can create enough heat in some instances to spontaneously combust and ignite the surrounding area. Lightning strikes the earth over 100,000 times a day. 10 to 20% of these lightning strikes can cause fire.</p>
                    </div>
                </div>
            </div>
  
</body>
<html>