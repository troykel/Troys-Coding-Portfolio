import java.util.*

fun main(Args:  Array<String>) {
    var sum = 0.0;
    var count = 0.0;
    val reader = Scanner(System.`in`)
    println("How many numbers do you want to average? ")
    var limit = reader.nextDouble()
    while (true) {
        print("Enter a number ")
        var num: Double = reader.nextDouble()
        var myList: List<Double> = mutableListOf(num)
        count += 1
        sum += num;
        var average = sum / count;
        print("\nSum = $sum")
        print("\nCount = $count")
        print("\n")
        print("Average = ")
        val s = String.format("%.2f", average)
        print(s)
        print("\n")
        if (count == limit)
            break;

    }
    var myList: List<Double> = mutableListOf()
    for (num: Double in myList)
        println("Your numbers are  $num")
    }
















