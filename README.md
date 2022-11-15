# BigData LoL<br/><br/>
**Environment erstellen (bei Ersterstellung):**
  
   bigdata_lol_env.yml - file herunterladen
  
```
  conda env create -f bigdata_lol_env.yml
  conda activate bigdata_lol
```

<br/>**Environment mit .yml-Datei aktualisieren:**

   bigdata_lol_env.yml - file herunterladen
  
```
  conda env update --prefix ./env --file bigdata_lol_env.yml  --prune 
```

<br/>**Environment in .yml-Datei speichern:**
<br/><br/>Mit ```conda env list``` sicherstellen, dass das bigdata_lol aktiv ist.
  
```
  conda env export > bigdata_lol_env.yml
```

# File Explanation
The main.ipynb is for the story Telling and includes only important parts related to that
The tasks.ipynb includes other tasks which did not help us in the Story Telling, but were done nonetheless. 
