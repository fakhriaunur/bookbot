{pkgs, ...}:

{
  languages.python = {
    enable = true;
    #version = "3.10.7";
    version = "3.12.0";

    venv.enable = true;
  };
}
