const { response } = require('express');
const https = require('https');
var cnt=0;
https.get('https://coderbyte.com/api/challenges/json/age-counting',function (response) {
    var x =''
   // console.log(response.statusCode);
    response.on('data', function(d) {
      x +=d;
      
    });
    response.on('end', () => {   
      var z =(JSON.parse(x).data);
     // console.log(x)
      var array = x.split(",");
      var cnt=0;
      for(var i=0;i<array.length;i++)
      {
        var z = array[i].split('=')
        if(z[0].trim()=='age')
        {
            var n = parseInt(z[1]);
            if(n>=50)
            {
                cnt++;
            }
        }
      }
     console.log(cnt)
    });
    
  })
.on('error', function(e) {
  console.error(e);
});
