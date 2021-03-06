# Homebrew formula file for deployment
class Proclip < Formula
  desc "A terminal / commandline extension capable of storing and executing frequently used commands conveniently"
  homepage "https://github.com/PhilJay/homebrew-proclip"


  url "https://github.com/PhilJay/homebrew-proclip.git", :using => :git, :tag => "0.1.4"

  def install
    # pcl is the name of the executable in the git repo
    bin.install "pcl"
  end
end
