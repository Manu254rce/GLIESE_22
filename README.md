# GLIESE_22

![pexels-drift-shutterbug-2085998](https://user-images.githubusercontent.com/69007849/208246475-093a974b-03e3-4b14-880f-ff161c19b6a4.jpg) 

## Basic Setup

addition of pip will be added later

### Using Conda

1. Clone this repository into your local machine:
```bash
git clone <repo url>
```

Or by PAT;

```bash
git clone https://<your PAT>@<repo url>
```

2. Install the required packages inside your conda env (ensure Conda is installed and set in PATH):

This should be run only once, to create the environment.

```bash
conda env create -f environment.yml

conda activate <env name>
```

I also created an automation script called `autoconf.py`, such that everytime you install a new package or remove an existing package, you can run the script to auto update the `environment.yml`. Note that this script is only for conda envs, I'll be adding a pip variant soon.

The -y flag is set to auto, hence to change it, edit `autoconf.py`

```bash
python autoconf.py <command> <package>
```

Commands: `install` or `remove`

### Using Docker

```bash
docker build -t gliese_22:tag .

docker run -it gliese_22:tag
```


## Usage

The python file can be run normally from any editor that supports version 3. You can also make use of the .ipynb file by running it in a Google Colab or Kaggle instance.





