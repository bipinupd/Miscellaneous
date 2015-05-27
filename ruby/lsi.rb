#longest increasing subsequene
#
#
def seperator
  puts "+++++++++Seperator++++++++++"
end

  mynumbers = [ 3,5,2,3,4,9,12,15,100,8]
  lsi=[]; #holds the longest increasing number till that index
  index=0;
  for number in mynumbers
    lsi.push(0)   #initialize everything to zero
  end
  puts mynumbers.join(" ") #prints on the same line with space as seperator
  seperator
=begin
lsi(index) = 1+ max(lsi(j)) => 0<j<index and mynumbers[j] > mynumbers[index]
else 1
=end
  for number in mynumbers 
  maxLsi=0;
  for j in 0..index
    if(mynumbers[index]>mynumbers[j] && maxLsi<lsi[j])
      maxLsi=lsi[j]      
    end
  end
  maxLsi=maxLsi+1;
  lsi[index]=maxLsi;
  index=index+1
  end
  puts lsi.join(" ") 
  seperator

