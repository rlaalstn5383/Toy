import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args){
// Read input string from standard input
    Scanner input = new Scanner(System.in);
    String equation = input.nextLine();
    input.close();
    
// Parse equation
    
    String[] words = parseEquation(equation);
    
    
// Remove duplicate alphabets
    SinglyLinkedList alphabets = removeDuplicates(words[0], words[1], words[2]);
// Solve
    SinglyLinkedList initialNumbers = new SinglyLinkedList();
    SinglyLinkedList assignedNumbers = solver(alphabets, initialNumbers, words[0], words[1], words[2]);
    
    
    Node alphabetNode = alphabets.getFirst();
    Node numberNode = assignedNumbers.getFirst();
    while (alphabetNode != null) {
      System.out.print((char)(alphabetNode.elem) + "=" + numberNode.elem + " ");
      alphabetNode = alphabetNode.next;
      numberNode = numberNode.next;
    }
  }
  
  public static String[] parseEquation(String s){
    String lowercase=s.toLowerCase();
    String L1 = "";
    String L2 = "";
    String R1 = "";
    String[] words = {L1, L2, R1};
    for(int j=0; j<3; j++){
      
      for(int i=0; i<s.length();i++){
        if(lowercase.charAt(i)=='='||lowercase.charAt(i)=='+'){
          j++;
        }
        else{
          if(97<=lowercase.charAt(i)&&lowercase.charAt(i)<=122){
            words[j]=words[j]+lowercase.charAt(i);
          }
        }
      }
    }
    
    return words;
  }
  
  public static SinglyLinkedList removeDuplicates(String L1, String L2, String L3) {
    SinglyLinkedList alphabets = new SinglyLinkedList();
    int count=0;
    String[] words={L1,L2,L3};
    alphabets.append((int)L1.charAt(0));
    
    for(int k=0; k<3; k++){
      for(int i=0;i<words[k].length();i++){
        if (corr_num (words[k].charAt(i), alphabets.getFirst (), alphabets.getFirst ()) == -100) {
          alphabets.append ((int) (words[k].charAt(i)));
        }
      }
    }
    //alphabets=sort(alphabets);
    return alphabets;
  }
  
  public static int corr_num(char a, Node aNode, Node nNode){
    if (aNode == null)
      return -100;
    if (aNode.elem == (int) a)
      return nNode.elem;
    return corr_num(a, aNode.next, nNode.next);
  }
  
  public static boolean checkAnswer(SinglyLinkedList alphabets, SinglyLinkedList assignedNumbers, String L1, String L2, String R1) {
    Node alphaNode = alphabets.getFirst();
    Node numNode = assignedNumbers.getFirst();
    while (alphaNode != null) {
      L1 = L1.replace(Character.toString((char) alphaNode.elem), String.valueOf(numNode.elem));
      L2 = L2.replace(Character.toString((char) alphaNode.elem), String.valueOf(numNode.elem));
      R1 = R1.replace(Character.toString((char) alphaNode.elem), String.valueOf(numNode.elem));
      alphaNode = alphaNode.next;
      numNode = numNode.next;
    }
    int left1sum = Integer.parseInt(L1);
    int left2sum = Integer.parseInt(L2);
    int right1sum = Integer.parseInt(R1);

    return (left1sum+left2sum==right1sum);
  }
  
  public static SinglyLinkedList sort(SinglyLinkedList list){
    Node e1= list.getFirst();
    SinglyLinkedList copy =new SinglyLinkedList();
    while(e1!=null){
      copy.append(e1.elem);
      e1=e1.next;
    }
    if(copy.size<=1){ return copy;}
    else{
      Node e=copy.getFirst();
      SinglyLinkedList left=new SinglyLinkedList();
      SinglyLinkedList right=new SinglyLinkedList();
      for(int i=0;i<copy.size/2;i++){
        left.append(e.elem);
        e=e.next;
      }
      for(int i=copy.size/2;i<copy.size;i++){
        right.append(e.elem);
        e=e.next;
      }
      left=sort(left);
      right=sort(right);
      copy=merge(left,right);
    }
    
    
    return copy;
  }
  public static SinglyLinkedList merge(SinglyLinkedList left,SinglyLinkedList right){
    SinglyLinkedList list=new SinglyLinkedList();
      
    while(left.isEmpty()==false&&right.isEmpty()==false){
      Node lefirst=left.getFirst();
      Node rifirst=right.getFirst();
      if(lefirst.elem<=rifirst.elem){
        list.append(lefirst.elem);
        left.remove(lefirst.elem);
      }
      else{
        list.append(rifirst.elem);
        right.remove(rifirst.elem);
      }
    }
    while(left.isEmpty()==false){
      Node lefirst=left.getFirst();
      list.append(lefirst.elem);
      left.remove(lefirst.elem);
    }
    while(right.isEmpty()==false){
      Node rifirst=right.getFirst();
      list.append(rifirst.elem);
      right.remove(rifirst.elem);
    }
    
    return list;
  }
// implement here
  
  
  public static SinglyLinkedList solve(int k,SinglyLinkedList save,SinglyLinkedList universe,SinglyLinkedList alphabets, SinglyLinkedList alphabets2, String L1,String L2, String R1 ){

    if (k == 0) {
      if(checkAnswer(alphabets,save,L1,L2,R1)==true)
        return save;
      else
        return null;
    }
    else {
      for (Node e = universe.getFirst(); e != null; e = e.next) {
        SinglyLinkedList ta1 = alphabets2.clone();
        SinglyLinkedList tsave = save.clone();
        tsave.append(e.elem);
        ta1.remove(ta1.getFirst().elem);
        SinglyLinkedList tuniverse = universe.clone();
        tuniverse.remove(e.elem);
        SinglyLinkedList ret = solve(k-1, tsave, tuniverse, alphabets, ta1, L1, L2, R1);
        if (ret != null)
          return ret;
      }
    }
    return null;
  }
  
  public static SinglyLinkedList solver(SinglyLinkedList alphabets, SinglyLinkedList assignedNumbers, String L1, String L2, String R1) {
    SinglyLinkedList universe= new SinglyLinkedList();
    for(int i=0; i<10; i++){
      universe.append(i);
    }
    int k=alphabets.size;
    SinglyLinkedList answer=solve(k,assignedNumbers,universe,alphabets,alphabets,L1,L2,R1);
    
    
    return answer;
  }
}


class Node {
  public int elem;
  public Node next;
  public Node(int e, Node n) {
    elem = e;
    next = n;
  }
}

class SinglyLinkedList{
  private Node first;
  private Node last;
  public int size;

  public SinglyLinkedList(){// constructor
    first = null;
    last = null;
    size = 0;
  }

  public boolean isEmpty() {
//implement here
    return size == 0;
  }

  public void append(int element){
  //implement here
    Node n = new Node(element, null);
    if (size == 0) {
      first = n;
      last = n;
    }
    else {
      last.next = n;
      last = n;
    }
    size++;
  }

  public void remove(int element){
    //implement here
    Node n = first;
    if (n == null)
      return;
    if (n.elem == element) {
      first = n.next;
      size--;
      return;
    }
    Node n2 = n.next;
    while (n2 != null) {
      if (n2.elem == element) {
        n.next = n2.next;
        size--;
        return;
      }
      n = n2;
      n2 = n2.next;
    }
  }

  public void printAll(){
    //implement here
    if(isEmpty()){
      System.out.println("");
    }
    else{
      Node curr=first;
      String output="";
      if(size==1) {
        System.out.println(curr.elem);
      }
      else{
        while(curr.next!=null){
          output=output+curr.elem+", ";
          curr=curr.next;
        }
        output=output+curr.elem;
      }
      System.out.println(output);
    }
  }

  public Node getFirst(){
    return first;
  }

  public void printNode(Node e){
    //implement here
    System.out.println("");
  }

  public SinglyLinkedList clone () {
    SinglyLinkedList ret = new SinglyLinkedList();
    Node cur = first;
    while (cur != null) {
      ret.append(cur.elem);
      cur = cur.next;
    }
    return ret;
  }

}
