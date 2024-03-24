from http.server import HTTPServer, BaseHTTPRequestHandler

content ="""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Herbal friend</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        .card
        {
            height:30rem;
            margin:10px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div style="background-color: rgb(182, 231, 210);">
    <div style="display: flex;font-size:20px;">
        <div>
            <img  style="height:150px;margin: 30px;" src="leaf.jpeg" alt="">
        </div>
        <div>
            <p style="font-size:65px;font-weight: bold;"><i>Greeny Herbals</i></p>
            <p>Make Your own medicine</p>
        </div>
        
        <div style="display:flex;padding-left: 350px;">
        <div style="padding:35px">Home</div>
        <div style="padding: 35px;">Herbs</div>
        <div style="padding: 35px;">About</div>
        <div style="padding:35px">Contact</div>
        
    </div>
    
    
</div>
</div>
<div style="display: flex;flex-direction:row; margin: 20px;border-radius:10px;" >
    
<div style="width:auto" id="carouselExampleFade" class="carousel slide carousel-fade">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img  style="height:700px;"  src="slidef.jpeg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img style="height:700px;"src="slidesecond.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img style="height:700px;" src="slideth.jpg" class="d-block w-100" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
</div>
<div style="display: flex;">
    <div class="card" style="width:18rem;">
        <img src="bucket.jpeg" class="card-img-top" alt="...">
        <div class="card-body">
            <h2>Special About Us</h2>
          <p class="card-text">Customers can search for their disease and know which herb is recommended to get cure speedy</p>
        </div>
      </div>
      <div class="card" style="width: 18rem;">
        <img src="food.jpg" class="card-img-top" alt="...">
        <div class="card-body">
            <h2>Yummy Medicine</h2>
          <p class="card-text">After choosing which herb is required to get cure,people can find recipes related to that herb.By doing this they get 100% natural medicine to their body without any chemicals added.</p>
        </div>
      </div>
 
</div>
</div>
  <div style="display:flex;">
    <div class="card" style="width: 18rem;">
        <img src="tulsi.avif" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Tulasi</h5>
          <p class="card-text">It boots your immune system.You can try new recipes with this magical herb.</p>
          <a href="#" class="btn btn-primary">Click</a>
        </div>
      </div>
  
  
    <div class="card" style="width: 18rem;">
        <img src="jelly.jpg" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">Jelly</h5>
          <p class="card-text">Healthy jelly made of 7 herbs to get cure cold.Children are being showing love to it</p>
          <a href="#" class="btn btn-primary">Click</a>
        </div>
      </div>
      <div class="card text-center">
        <div class="card-header">
          Orders
        </div>
        <div class="card-body">
          <h5 class="card-title">If your are lazy to make your recipes we are here to help you! You can make use of our herbicana.</h5>
          <p class="card-text">Click below to place your order</p>
          <a href="#" class="btn btn-primary">Ding ding</a>
        </div>
        <div class="card-footer text-body-secondary">
          Herbicana a mobile app to place order.
          The order may thing like dishes,oils,soaps,herbal tablets etc.
        </div>
      </div>
  </div>
</div>
  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>
"""
class myhandler (BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received") 
        self.send_response (200)

        self.send_header('content-type', 'text/html; charset=utf-8')

        self.end_headers()

        self.wfile.write(content.encode())





server_address = ('',8000)

httpd = HTTPServer(server_address, myhandler)

print("my webserver is running...")

httpd.serve_forever()

