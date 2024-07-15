 # un body dove il css impone il testo centrato
# nel body mettere una griglia (grid layout di bootstrap)
# le colonne della griglia sono delle card .                        
# Dividere la pagina html in tre blocchi, chiamati pag11 pag12 pag13 in modo che valga la seguente relazione pag = pag11 + N*pag12 + pag13. 
# Per costruire i tre blocchi tenere conto di quanto discusso in classe. Creare un semplice script in python che, assegnato un numero ad N, es. N = 3 genera la pagina html.  
pag11 = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>STRESS</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
<link rel="icon" href="imgs/stress.jpg">
     <link rel="icon" href=".png">

  </head>
  <body>
    <style>
        

        main{
        margin-top: 20px;
        margin-right: 20px;
        margin-left: 20px;
        font-family: sans-serif;
        }

        .container-fluid {background-color: silver;
    list-style-type: none;
    padding: 10px;
    margin: 0px;
    overflow: hidden;}


    </style>

  <nav class="navbar bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand">Troppo stressati?</a>

  </div>
</nav>
<main>
    <center>
      <div class="container text-center">
        <div class="row">
"""

pag12 = """
          <div class="col-md-4">
            <div class="card" style="width: 18rem;">
              <img src="imgs/stress.jpg" class="card-img-top" alt="..." width="175px" height="180px">
              <div class="card-body">
                <h5 class="card-title">STRESS</h5>
                <p class="card-text">Lo stress è una reazione che si manifesta quando un organismo percepisce uno squilibrio tra le sollecitazioni ricevute e le risorse a disposizione. Si tratta, precisamente, di una sindrome generale di adattamento (SGA) atta a ristabilire un nuovo equilibrio interno (omeostasi) in seguito a fattori di stress (in inglese detti stressor). Le alterazioni dell'equilibrio interno possono avvenire a livello endocrino, umorale, organico, biologico. Il termine stress venne introdotto per la prima volta in biologia da Walter Bradford Cannon nel 1935; la sindrome venne definita in questo modo da Hans Selye nel 1936.</p>
                <button class="btn btn-primary"><a href="#" class="text-white">Pulsante anti-stress</a></button>
              </div>
            </div>
          </div>
"""

pag13 = """
        </div>
      </div>
    </center>
    </main>
  </body>
</html>
"""

n = int(input("inserisci il numero da moltiplicare: "))
pag = pag11 + (n * pag12) + pag13

with open("risultato.html", "w") as file:
    file.write(pag)