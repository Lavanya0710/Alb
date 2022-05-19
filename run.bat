REM pytest -v -s -m "sanity" --html=Reports\sanityreport.html TestCase/
rem pytest -v -s -m "sanity and regression" --html=Reports\sanityandregressionreport.html TestCase/
rem pytest -v -s -m "sanity or regression" --html=Reports\sanityorregressionreport.html TestCase/ 
pytest -v -s -m "regression" --html=Reports\regressionreport.html TestCase/

