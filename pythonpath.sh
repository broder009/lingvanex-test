basedir=$(pwd)
filters="/filters/"
preprocessors="/preprocessors/"
filters_path="$basedir""$filters"
preprocessors_path="$basedir""$preprocessors"
export PYTHONPATH="${PYTHONPATH}:$filters_path"
export PYTHONPATH="${PYTHONPATH}:$preprocessors_path"