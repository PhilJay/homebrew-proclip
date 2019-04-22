class Proclip < Formula
  desc "A terminal / commandline extension capable of storing and executing frequently used commands conveniently"
  homepage "https://github.com/PhilJay/homebrew-proclip"


  url "https://github.com/PhilJay/homebrew-proclip.git", :using => :git, :tag => "0.1.0"

  def install
    # the name of the executable in the git repo
    bin.install "pcl"
  end
end
