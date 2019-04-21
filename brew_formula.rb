class BrewFormula < Formula
  desc "A terminal / commandline extension capable of storing and executing frequently used commands conveniently"
  homepage "https://github.com/PhilJay/homebrew-proclip"


  url "https://github.com/PhilJay/homebrew-proclip/blob/master/proclip", :using => :curl, :tag => "0.0.1"

  def install
    bin.install "philjay/proclip"
  end
end
