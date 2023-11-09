{pkgs, ...}:

{
  languages.python = {
    enable = true;
    version = "3.10.7";

    venv.enable = true;
  };
}
