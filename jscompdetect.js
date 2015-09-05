setInterval(function()
	{     
		console.log("URI :" + document.baseURI);
		console.log("No of scripts : " + document.scripts.length);
		for ( i= 0 ; i < document.scripts.length ;i++)
		{
			console.log("Script #" + i + ":" + document.scripts[i].src);
			console.log("Script text :" + document.scripts[i].text);
		} 
		/*var windowframes = window.frames;
		console.log("No of iframes #" + windowframes.length);
		for ( j=0 ; j < windowframes.length; j++)
		{
			console.log("Frame # " + j + " src = " + window.frames[j].src); 
			console.log("No of scripts in iframe = " + window.frames[j].scripts.src);
		}*/
	}, 3000);
