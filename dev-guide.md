
# 5 minute guide for YASS developers

## 1. Paths

* Use CONFIG.path_to_output_directory
* Use pathlib str(path / to / file)

### 2. YASS configuration file

* Do not add new parameters

## 3. Customizing the default pipeline

* Create a new script (use x.py as template)
* Do not modify [step name]/run.py
* When adding new algorithms, create a function that conforms to the api and do something like

```python
results = cluster.run(method=fancy_new_method)
```

## 4. git branches

* Master is for well-tested code (merges via pull request)
* dev if for tested code that still needs cleanup (merges via pull request)
* Every other branch can fail
* Merge from master continously to get the latest maintenance features


# Other tools

* Profiling
* Testing other datasets
* Benchmarking