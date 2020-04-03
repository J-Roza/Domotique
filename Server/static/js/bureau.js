function toggle_bureau()
{
    var url = "/toggle_yeelight/0";
    call_url(url);
    url = "/toggle_yeelight/1";
    call_url(url);
}

function call_url(url)
{
    var req = new XMLHttpRequest();
    req.open("GET", url, true);
    req.send(null);
}

window.onload = check_state();
function check_state()
{
    var url = "/check_state_yeelight/";
    fetch(url).then(function(response) 
    {
        if (response.status !== 200) 
        {
            console.log(`Looks like there was a problem. Status code: ${response.status}`);
            return;
        }
        response.json().then(function(data) 
        {
            //console.log(data.properties.bulb0.power, data.properties.bulb1.power);
            //bulb trepied
            var state_bulb0 = data.properties.bulb0.power;
            //bulb etagere
            var state_bulb1 = data.properties.bulb1.power;

            var state_arr = [state_bulb0, state_bulb1];
            handle_state(state_arr);
        });
    })
        .catch(function(error) 
        {
            console.log("Fetch error: " + error);
        });
};

//envoi url pour allumer les bulbs et refresh la page 
function create_img(path, id_bulb)
{ 
    var img = document.createElement('img');
    img.src = path;
    img.onclick = function()                        
    {
        call_url("/toggle_yeelight/" + id_bulb);
        // Recharge la page actuelle, sans utiliser le cache
        document.location.reload(true);
    };
    return img;
}

//Créé et Change img en fonction de l'etat (on/off)
function handle_state(state_bulb_list) 
{
    for (i = 0; i < state_bulb_list.length; i++)
    {
        var img = document.createElement('img');
        img = create_img("/static/img/light_bulb_" + state_bulb_list[i] + "_" + i + ".png", i);                  
        document.getElementById("bulb_div_" + i).appendChild(img);
    };
    
} 


//Variateur de couleur
function watchColorPicker(event)
{
    var rgb_col = document.getElementById("rgb").value;
    call_url("/start_color_cycle_yeelight/0/" + rgb_col.slice(1));
    call_url("/start_color_cycle_yeelight/1/" + rgb_col.slice(1));
}


//Horloge
function drawClock() 
{
  drawFace(ctx, radius);
  drawNumbers(ctx, radius);
  drawTime(ctx, radius);
}

function drawFace(ctx, radius) 
{
  var grad;
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, 2*Math.PI);
  ctx.fillStyle = 'white';
  ctx.fill();
  grad = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05);
  grad.addColorStop(0, '#333');
  grad.addColorStop(0.5, 'white');
  grad.addColorStop(1, '#333');
  ctx.strokeStyle = grad;
  ctx.lineWidth = radius*0.1;
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, radius*0.1, 0, 2*Math.PI);
  ctx.fillStyle = '#333';
  ctx.fill();
}

function drawNumbers(ctx, radius) 
{
  var ang;
  var num;
  ctx.font = radius*0.15 + "px arial";
  ctx.textBaseline="middle";
  ctx.textAlign="center";
  for(num = 1; num < 13; num++)
  {
    ang = num * Math.PI / 6;
    ctx.rotate(ang);
    ctx.translate(0, -radius*0.85);
    ctx.rotate(-ang);
    ctx.fillText(num.toString(), 0, 0);
    ctx.rotate(ang);
    ctx.translate(0, radius*0.85);
    ctx.rotate(-ang);
  }
}

function drawTime(ctx, radius)
{
    var now = new Date();
    var hour = now.getHours();
    var minute = now.getMinutes();
    var second = now.getSeconds();
    //hour
    hour=hour%12;
    hour=(hour*Math.PI/6)+
    (minute*Math.PI/(6*60))+
    (second*Math.PI/(360*60));
    drawHand(ctx, hour, radius*0.5, radius*0.07);
    //minute
    minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
    drawHand(ctx, minute, radius*0.8, radius*0.07);
    // second
    second=(second*Math.PI/30);
    drawHand(ctx, second, radius*0.9, radius*0.02);
}

function drawHand(ctx, pos, length, width) 
{
    ctx.beginPath();
    ctx.lineWidth = width;
    ctx.lineCap = "round";
    ctx.moveTo(0,0);
    ctx.rotate(pos);
    ctx.lineTo(0, -length);
    ctx.stroke();
    ctx.rotate(-pos);
}