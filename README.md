# Computer-Vision-Assignment


**TASK:**

The year is 2500 and the Earth is under attack from aliens, intent on stripping the planet of its natural
resource of polydimethylsiloxane. You have just experienced the worst solar flare in living memory, which
has wiped out the Earth’s automatic defence system. . . and that means that the buck stops with you as Chief
Scientist of the Earth Defence Corps.
A lowly technician, one Adrian Clark, has just sent you a message. He says the long-range cameras on
Nyx and Styx, two of the moons of Pluto, have detected a meteor shower coming from the Oort Cloud and
he is concerned that an alien vessel is hiding amongst the meteors. The aliens have tried this kind of thing
before — it is usually easy to spot alien craft as they have to manoeuvre to avoid the meteors, whereas the
meteors themselves travel in straight lines. Surely it cannot be too difficult to knock together a program
to identify any meteor exhibiting non-linear motion in 3D?
The trouble is that the solar flare knocked out all modern computers. Looking around, you realise with
horror that the only computer that has survived the flare unscathed is one of your antiques, a 2020s-vintage
PC running Linux. Booting it and logging in, you see that you have support for only Python, so you will
have to program a solution using that. You also have copies of numpy and the OpenCV library from the
same period, which you know will be able to handle the images from the long-range scanner.
You sigh deeply and reply to Adrian Clark: “Send me the imagery and I’ll try to write some software to
report anything that manoeuvres in the meteor shower.”
“OK,” he messages back. “We have only low-resolution imagery from two cameras; thankfully they are
identical. The telescopes to which the cameras are attached have focal lengths of 12 m and are arranged
3.5 km apart with their optical axes exactly aligned. The cameras have a 10-micron pixel spacing. I have
50 frames captured simultaneously from the left and the right cameras, which I’ll put into a zip-file and
send to you. I reckon you have until just before noon on Tuesday 23 rd March before the meteors reach
Earth. You have to make your program work by then.” Mentally, you roll your sleeves up before turning to
the keyboard and starting up Emacs. If the situation wasn’t so serious, this would be fun. . .
