<template>
	<lorem add="20p"></lorem>	
</template>

<script>
import LoremIpsum from "vue-lorem-ipsum";
export default {
	name: "Home",
	components: {
		lorem: LoremIpsum
	}
};
</script>