class BrewFormula < Formula
  desc "A terminal / commandline extension capable of storing and executing frequently used commands conveniently"
  homepage "https://github.com/PhilJay/ProClip"


  url "https://github.com/PhilJay/ProClip/blob/master/proclip", :using => :curl

  def install
    bin.install "philjay/proclip"
  end
end
