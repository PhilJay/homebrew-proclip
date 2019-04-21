class BrewFormula < Formula
  desc "A terminal / commandline extension capable of storing and executing frequently used commands conveniently"
  homepage "https://github.com/PhilJay/homebrew-proclip"


  url "https://github.com/PhilJay/homebrew-proclip.git", :using => :git, :tag => "0.0.2"

  def install
    bin.install "proclip"
  end
end
