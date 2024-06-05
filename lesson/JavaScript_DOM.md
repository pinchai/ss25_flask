## What is the DOM?

### The DOM stands for Document Object Model.

<img src="https://www.freecodecamp.org/news/content/images/2021/01/images.png" style="border-radius: 10px; width: 500px"/>

## How to Select Elements in the DOM

```javascript
<p id="master">i love javascript</p>

<script>
    const masterEl = document.getElementById('master')
    console.log(masterEl) //
    <p id="master">i love javascript</p>
</script>
```

```javascript
        <p class="master2">i love javascript</p>
<p class="master2">i love react</p>
<h1 class="master2">i want a job</h1>

<button id="btn">click me</button>

<script>

    const btn = document.getElementById('btn')

    btn.addEventListener('click', function master(){
    var master = document.getElementsByClassName("master2");
    master[2].innerHTML = 'i need a job';
})

</script>
```

## addEventListener

```javascript
<p>VsCode</p>
<p>Atom</p>
<p>Sublime text</p>
<button id="btn">click me</button>


<script>

    const btn = document.getElementById('btn')

    btn.addEventListener('click', function master(){
    let master = document.getElementsByTagName('p');
    let masterEl = master[1].innerHTML = 'Code editors';
    console.log(masterEl) //Code editors
})

    //
    <p>Atom</p>
    changes to
    <p>Code editors</p>
</script>
```

## How to Select DOM Elements with CSS Selectors

.querySelector()

```javascript
<div id=master>i am a frontend developer</div>

<script>
    const master = document.querySelector("#master")
</script>
```

## .querySelectorAll()

```javascript
<p class="master">React</p>
<p class="master">Vue</p>
<p class="master">Angular</p>

<script>
    const master = document.querySelectorAll(".master")
    console.log(master[1]) //
    <p class="master">Vue</p>
</script>
```

## How to Append an Element

```javascript
const createEl = document.createElement('div')

const innerhtml = createEl.innerHTML = 'i am a frontend developer'

const parentEl = document.getElementById('parent')

parentEl.appendChild(createEl)

console.log(parentEl) 
```

## How to Remove a Child Element

```javascript
const firstchildEl = document.getElementById('firstchild')
const parentEl = document.getElementById('parent')

parentEl.removeChild(firstchildEl)

console.log(parentEl)
```
