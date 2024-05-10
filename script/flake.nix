{
	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
	};

	outputs = { self, nixpkgs }:
	  let
	    system = "x86_64-linux";
	    name = "dev shell";
	    src = "./.";
	    pkgs = nixpkgs.legacyPackages.${system};
	  in
	  {
	  	packages.${system}.default = derivation {
	  		inherit system name src;
	  		builder = with pkgs; ""
	  	}
	  }
}
