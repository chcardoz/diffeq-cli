# CLI for creating and visualizing Differential Equations.

## Instructions
Clone the repository
```bash
git clone https://github.com/chcardoz/diffeq-cli.git nonlinear
```
This creates a directory called nonlinear with a .git inside it. You can delete the .git if you want to. 

Go into the directory
```bash
cd nonlinear
```

Than you will need to create a python virtual environment. Having a python virtual environment will allow you to cleanly install the dependencies and delete the virtual environment when you are done without any junk in your computer. 
```bash
python3 -m venv venv
```

Build from source the activate script of the virtual environment
```bash
source venv/bin/activate
```

Now, you are in the virtual environment. To get out, you can always do
```bash
deactivate
```

Once you are inside the virtual environment, you have to install the package in development mode
```bash
pip install -e .
```
The -e flag stands for editable, which means you are in development mode and any edits you make to the source code show up immediately without you building the project again. 

All of the above was just so we can do this
```
solution --help
```
You get your own command line interface to solve the equation. You can go into the solution directory and check the init file to see the code. 
