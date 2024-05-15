{
  pkgs ? import <nixpkgs> { },
}:
with pkgs;
mkShellNoCC {
  packages = [
    python311
    python311Packages.matplotlib
  ];

  shellHook = ''
      echo "hello, world!"
  '';
}
