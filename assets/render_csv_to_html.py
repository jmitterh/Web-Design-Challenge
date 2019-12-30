import pandas as pd
#import webbrowser

df = pd.read_csv("../Resources/cities.csv")
print(df.head())

data_html = open('../dataset.html','w')

message = f"""
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>Data</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.3/examples/starter-template/">

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <!-- styles sheet -->
    <link rel="stylesheet" type="text/css" href="./visualization/styles.css">

</head>

<body>
<main role="main" class="container">
    <div class='row'>
        <div class="col-md-12">
            <!-- Navbar -->
            <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
                <a class="navbar-brand" href="index.html">Lattitude</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse"
                        data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false"
                        aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarsExampleDefault">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="index.html">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="comparison.html">Comparison</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="dataset.html">Data <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown"
                               aria-haspopup="true" aria-expanded="false">Plots</a>
                            <span class="caret"></span>
                            <div class="dropdown-menu" aria-labelledby="dropdown01">
                                <a class="dropdown-item" href="./visualization/temp.html">Max Temperature</a>
                                <a class="dropdown-item" href="./visualization/humidity.html">Humidity</a>
                                <a class="dropdown-item" href="./visualization/cloudiness.html">Cloudiness</a>
                                <a class="dropdown-item" href="./visualization/wind_speed.html">Wind Speed</a>
                            </div>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    </div>
    <!-- End of Nav -->
    <div id="top_body" class='row'>
        <div class="col-lg-12 col-md-12">
            <!-- large container -->
                <p id="paragraph_p">
                    The following table includes all of the data used for plotting during this project.
                </p>
                {df.to_html(index=False)}
        </div>
    </div>

    <!-- Footer -->
    <footer class="page-footer font-small blue">

        <!-- Copyright -->
        <div class="footer-copyright text-center py-3">
            © 2019 Jean-Paul M. Copyright
        </div>
        <!-- Copyright -->

    </footer>
    <!-- Footer -->


</main><!-- /.container -->

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
        crossorigin="anonymous"></script>

</body>

</html>

"""
data_html.write(message)
data_html.close()
