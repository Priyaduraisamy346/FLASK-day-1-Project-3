from flask import Flask
app=Flask(__name__)
@app.route('/')
def project():
    return "<h1 style='background:powderblue'><center>My first routing page</center></h1><hr><h2 style='color:Sienna'><center>The Pig and the Sheep</center></h2><p style='color:black'>A pig found its way into a meadow where a shepherd was grazing a herd of sheep. The shepherd caught the pig and carried him off toward the butcher shop when it started crying loud and struggled to get free. The sheep told the pig, The shepherd catches us regularly and drags us off like that, and we don't make any noise. The pig replied, My case and yours are altogether different; he catches and takes you to shave off the wool, but he wants me to be killed for making the bacon.<br><br><br><b>Moral:<br>Do'not compare two situations without understanding them.</p>"

@app.route('/abc')
def project1():
     return "<h1 style='background:powderblue'><center>My second routing page</center></h1><hr><h2 style='color:Sienna'><center> The King’s Painting </center></h2><p style='color:black'>There was a king with only one leg and one eye but was generous and competent as a ruler. One day while walking in his palace, the king noticed the portraits of his ancestors along the hallway. He also wanted his portrait painted by an artist but was unsure how it would turn out due to his physical abnormalities. The King invited all the painters across the kingdoms and asked who could paint a beautiful picture of him. The painters were confused about how to make a beautiful picture of the King with only one leg and one eye.All the painters politely refused to make a painting of the King. Then one young painter came forward and ensured to make a beautiful portrait of the King. After a few days, the young painter unveiled the portrait in the court in which the King was seen sitting on the horse with one leg visible, holding his bow and aiming the arrow with one eye closed. There was no sign of physical deficiencies in the king in the painting. The King was pleased to see that the painter had creatively presented the King’s positive characteristics but not highlighted the abnormalities.<br><br><br><b>Moral:<br>Look at the positive aspects of someone without emphasizing the limitations.</p>"

if __name__=='__main__':
    app.run(debug=True)
